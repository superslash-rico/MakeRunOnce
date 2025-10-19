import requests
import json


def run_make_scenario(zone_url, api_token, scenario_id, data=None):
    """
    运行 Make.com 场景
    
    参数:
        zone_url: Make.com 区域URL (如 us1.make.com)
        api_token: API Token
        scenario_id: 场景 ID
        data: 可选的数据字典
    
    返回:
        响应数据字典
    """

    # 构建完整的 API URL
    api_url = f"https://{zone_url}/api/v2/scenarios/{scenario_id}/run"

    # 设置请求头
    headers = {
        "Authorization": 'Token ' + api_token,
        "Content-Type": "application/json"
    }

    # 准备请求体
    payload = {
        "data": data if data else {},
        "responsive": False,
        "callbackUrl": ""
    }

    try:
        # 打印调试信息
        print(f"API URL: {api_url}")
        print(f"Headers: {headers}")
        print(f"Payload: {json.dumps(payload, indent=2)}")
        
        # 发送 POST 请求
        response = requests.post(api_url,
                                 headers=headers,
                                 data=json.dumps(payload),
                                 timeout=30)

        print(f"Response Status: {response.status_code}")
        print(f"Response Headers: {dict(response.headers)}")
        print(f"Response Text: {response.text}")

        # 检查响应状态
        response.raise_for_status()

        # 返回 JSON 响应
        return {
            "success": True,
            "status_code": response.status_code,
            "data": response.json() if response.text else {}
        }

    except requests.exceptions.HTTPError as e:
        error_details = {
            "success": False,
            "error": f"HTTP 错误: {e.response.status_code}",
            "message": e.response.text,
            "url": api_url,
            "status_code": e.response.status_code
        }
        
        # 针对403错误提供更具体的诊断信息
        if e.response.status_code == 403:
            error_details["diagnosis"] = {
                "possible_causes": [
                    "API Token 无效或已过期",
                    "API Token 权限不足",
                    "Scenario ID 不存在或无权限访问",
                    "Zone URL 不正确",
                    "账户权限限制"
                ],
                "suggestions": [
                    "检查 API Token 是否正确且有效",
                    "确认 API Token 有运行场景的权限",
                    "验证 Scenario ID 是否正确",
                    "确认 Zone URL 格式正确（如：us1.make.com）",
                    "检查 Make.com 账户是否有足够权限"
                ]
            }
        
        print(f"HTTP Error Details: {json.dumps(error_details, indent=2)}")
        return error_details
    except requests.exceptions.Timeout:
        return {
            "success": False,
            "error": "请求超时",
            "message": "Make.com API 请求超时，请稍后重试"
        }
    except requests.exceptions.RequestException as e:
        return {"success": False, "error": "请求失败", "message": str(e)}
    except json.JSONDecodeError:
        return {"success": False, "error": "JSON 解析错误", "message": "无法解析响应数据"}


if __name__ == "__main__":
    # 测试示例
    result = run_make_scenario(zone_url="us1.make.com",
                               api_token="YOUR_API_KEY",
                               scenario_id="YOUR_SCENARIO_ID",
                               data={"test": "value"})
    print(result)
