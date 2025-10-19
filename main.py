from flask import Flask, render_template, request, jsonify
# from playground.search_and_replace import search_and_replace_func
from playground.make import run_make_scenario
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/search_and_replace')
# def search_and_replace():
#     try:
#         search_and_replace_func('abc', '123')
#         return '替换操作执行成功！所有 "abc" 已替换为 "123"'
#     except Exception as e:
#         error_message = str(e)
#         print(f"替换操作失败: {error_message}")
#         
#         if "UnmarshalException" in error_message:
#             return f'API 数据格式不匹配错误。这可能是因为 SDK 版本与 API 不兼容。建议检查 baseopensdk 版本。', 500
#         elif "APP_TOKEN" in error_message or "PERSONAL_BASE_TOKEN" in error_message or "TABLE_ID" in error_message:
#             return '缺少必要的环境变量配置（APP_TOKEN, PERSONAL_BASE_TOKEN, TABLE_ID）', 500
#         else:
#             return f'替换操作失败: {error_message}', 500

@app.route('/make_run', methods=['POST'])
def make_run():
    try:
        data = request.json
        zone_url = data.get('zone_url')
        api_token = data.get('api_token')
        scenario_id = data.get('scenario_id')
        scenario_data = data.get('data')
        
        if not zone_url or not api_token or not scenario_id:
            return jsonify({
                'success': False,
                'error': '缺少必要参数'
            }), 400
        
        # 如果 scenario_data 是字符串，尝试解析为 JSON
        if scenario_data and isinstance(scenario_data, str):
            try:
                scenario_data = json.loads(scenario_data)
            except json.JSONDecodeError:
                scenario_data = None
        
        result = run_make_scenario(zone_url, api_token, scenario_id, scenario_data)
        
        if result['success']:
            return jsonify(result)
        else:
            return jsonify(result), 500
            
    except Exception as e:
        return jsonify({
            'success': False,
            'error': '运行失败',
            'message': str(e)
        }), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9261, debug=True)
