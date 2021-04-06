"""
간단한 웹 클라이언트
"""
import urllib.request

print(urllib.request.urlopen("http://www.naver.com").read().decode('utf-8'))

