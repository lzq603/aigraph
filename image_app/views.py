from django.shortcuts import render
from django.http import JsonResponse
import time
from image_app import chat_fun
import traceback
from requests.exceptions import ProxyError
from openai.error import APIConnectionError, RateLimitError
import subprocess
import base64
import binascii

visitCount = 0

def generate_image(request):
    global visitCount
    if request.method == 'POST':
        description = request.POST.get('description')
        print(description)
        err_msg = ''
        
        try:
            filename = chat_fun.gen_funart(text=description)
        except APIConnectionError as e:
            error_msg = str(e)
            if error_msg.find("Caused by ProxyError") >= 0:
                print("代理错误")
                proc = subprocess.Popen('supervisorctl restart clash', shell=True)
                proc.wait()
                try:
                    filename = chat_fun.gen_funart(text=description)
                except Exception as e:
                    err_msg = '生成失败，请调整提示词'
            else:
                print("API错误")
                filename = 'static/images/failed.jpeg'
                traceback.print_exc()
                filename = ''
                err_msg = '生成失败，请调整提示词'
        except Exception as e:
            print("其他错误")
            traceback.print_exc()
            err_msg = '生成失败，请调整提示词'
            filename = 'static/images/failed.jpeg'

        # 在实际应用中，这里应该返回生成的图像的路径
        image_path = 'static/function_art/' + filename + '.png'

        return JsonResponse({'image_path': image_path, 'error': err_msg})
    visitCount += 1
    return render(request, 'generate_image.html', context={'visitCount': visitCount})


def generate_graph(request):

    def decrypt(encrypted_base64, key):
        # 解码Base64
        encrypted_bytes = base64.b64decode(encrypted_base64.encode('utf-8'))
        encrypted_text = encrypted_bytes.decode('utf-8')
    
        decrypted_text = ""
        for char in encrypted_text:
            decrypted_char = ord(char) ^ key  # 对字符的ASCII码与密钥进行异或运算
            decrypted_text += chr(decrypted_char)
        return decrypted_text

    global visitCount
    if request.method == 'POST':

        api_key = request.GET.get("apikey", "")
        print(api_key)

        description = request.POST.get('description')
        print(description)
        err_msg = ''

        try:
            script = chat_fun.gen_graph(text=description, api_key=decrypt(api_key, 42))
        except APIConnectionError as e:
            error_msg = str(e)
            if error_msg.find("Caused by ProxyError") >= 0:
                print("代理错误")
                proc = subprocess.Popen('supervisorctl restart clash', shell=True)
                proc.wait()
                try:
                    script = chat_fun.gen_graph(text=description)
                except Exception as e:
                    err_msg = '生成失败，请调整提示词'
            else:
                print("API错误")
                script = "alert('生成失败')"
                traceback.print_exc()
                err_msg = '生成失败，请调整提示词'
        except binascii.Error as e:
            print("错误的KEY")
            traceback.print_exc()
            err_msg = '输入的KEY不正确请检查'
            script = "alert('请检查KEY是否正确')"
        except RateLimitError as e:
            print("账户额度不足")
            traceback.print_exc()
            err_msg = '账户额度不足'
            script = "alert('账户额度不足')"
        except Exception as e:
            print("其他错误")
            traceback.print_exc()
            err_msg = '生成失败，请调整提示词'
            script = "alert('生成失败')"

        return JsonResponse({'script': script, 'error': err_msg})
    visitCount += 1
    return render(request, 'generate_graph.html', context={'visitCount': visitCount})
