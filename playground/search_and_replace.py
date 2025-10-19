from baseopensdk import BaseClient
from baseopensdk.api.base.v1 import *
import os
import requests
import json

APP_TOKEN = os.environ.get('APP_TOKEN', '')
PERSONAL_BASE_TOKEN = os.environ.get('PERSONAL_BASE_TOKEN', '')
TABLE_ID = os.environ.get('TABLE_ID', '')


def search_and_replace_func(source: str, target: str):
  """使用混合方式：SDK 获取记录，直接 API 调用获取字段（避免兼容性问题）"""
  
  # 检查环境变量
  if not APP_TOKEN or not PERSONAL_BASE_TOKEN or not TABLE_ID:
    raise ValueError("缺少必要的环境变量：APP_TOKEN, PERSONAL_BASE_TOKEN 或 TABLE_ID")
  
  # 1. 使用 SDK 构建客户端
  client: BaseClient = BaseClient.builder() \
    .app_token(APP_TOKEN) \
    .personal_base_token(PERSONAL_BASE_TOKEN) \
    .build()

  # 2. 使用直接 API 调用获取字段（绕过 SDK 的解析问题）
  # 使用 SDK 配置的域名：base-api.feishu.cn（专用于 personal base token）
  base_url = "https://base-api.feishu.cn/open-apis/bitable/v1"
  
  # 使用 personal base token 作为认证
  headers = {
    "Authorization": f"Bearer {PERSONAL_BASE_TOKEN}",
    "Content-Type": "application/json"
  }
  
  # 尝试获取字段列表 - 使用原始 JSON 响应
  fields_url = f"{base_url}/apps/{APP_TOKEN}/tables/{TABLE_ID}/fields?page_size=100"
  fields_response = requests.get(fields_url, headers=headers)
  
  if fields_response.status_code != 200:
    print(f"API 错误: {fields_response.text}")
    raise Exception(f"API 调用失败: {fields_response.text}")
  
  fields_data = fields_response.json()
  
  # 手动解析字段，跳过有问题的 description
  text_field_names = []
  for field in fields_data.get('data', {}).get('items', []):
    if field.get('ui_type') == 'Text':
      text_field_names.append(field.get('field_name'))

  # 3. 获取记录列表（使用 SDK）
  list_record_request = ListAppTableRecordRequest.builder() \
    .page_size(100) \
    .table_id(TABLE_ID) \
    .build()

  list_record_response = client.base.v1.app_table_record.list(list_record_request)
  records = getattr(list_record_response.data, 'items') or []

  # 4. 处理需要更新的记录
  records_need_update = []

  for record in records:
    record_id, fields = record.record_id, record.fields
    new_fields = {}

    for key, value in fields.items():
      if key in text_field_names and isinstance(value, str):
        new_value = value.replace(source, target)
        if new_value != value:
          new_fields[key] = new_value

    if new_fields:
      records_need_update.append({
        "record_id": record_id,
        "fields": new_fields
      })

  print(f"找到 {len(records_need_update)} 条需要更新的记录")

  # 5. 批量更新记录（使用 SDK）
  if records_need_update:
    batch_update_records_request = BatchUpdateAppTableRecordRequest().builder() \
      .table_id(TABLE_ID) \
      .request_body(
        BatchUpdateAppTableRecordRequestBody.builder() \
          .records(records_need_update) \
          .build()
      ) \
      .build()
    batch_update_records_response = client.base.v1.app_table_record.batch_update(
      batch_update_records_request)
    print('替换成功！')
  else:
    print('没有找到需要替换的内容')


if __name__ == "__main__":
  # replace all 'abc' to '233333'
  search_and_replace_func('abc', '233333')
