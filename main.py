#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import pyaes
import base64
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.core.clipboard import Clipboard
from kivy.metrics import dp


class AESUtils:
    """AES加密解密工具类"""

    @staticmethod
    def pad(data):
        """PKCS7 padding"""
        padding_len = 16 - (len(data) % 16)
        return data + bytes([padding_len] * padding_len)

    @staticmethod
    def unpad(data):
        """去除PKCS7 padding"""
        padding_len = data[-1]
        return data[:-padding_len]

    @staticmethod
    def encrypt(plaintext, key, iv):
        """AES加密"""
        try:
            key_bytes = key.encode('utf-8')
            iv_bytes = iv.encode('utf-8')
            data_bytes = AESUtils.pad(plaintext.encode('utf-8'))

            aes = pyaes.AESModeOfOperationCBC(key_bytes, iv=iv_bytes)
            encrypted = aes.encrypt(data_bytes)
            return base64.b64encode(encrypted).decode('utf-8'), None
        except Exception as e:
            return None, str(e)

    @staticmethod
    def decrypt(encrypted_base64, key, iv):
        """AES解密"""
        try:
            key_bytes = key.encode('utf-8')
            iv_bytes = iv.encode('utf-8')
            encrypted_bytes = base64.b64decode(encrypted_base64)

            aes = pyaes.AESModeOfOperationCBC(key_bytes, iv=iv_bytes)
            decrypted = aes.decrypt(encrypted_bytes)
            return AESUtils.unpad(decrypted).decode('utf-8'), None
        except Exception as e:
            return None, str(e)


class EncryptTab(BoxLayout):
    """加密标签页"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = dp(10)
        self.spacing = dp(10)

        # 明文输入
        self.add_widget(Label(text='明文:', size_hint_y=None, height=dp(30)))
        self.plaintext_input = TextInput(
            multiline=True,
            size_hint_y=None,
            height=dp(100),
            hint_text='输入要加密的内容'
        )
        self.add_widget(self.plaintext_input)

        # 密钥输入
        self.add_widget(Label(text='密钥 (Key) - 16字节:', size_hint_y=None, height=dp(30)))
        self.key_input = TextInput(
            text='844dd1be967b6e9e',
            size_hint_y=None,
            height=dp(40),
            hint_text='输入16字节密钥'
        )
        self.add_widget(self.key_input)

        # IV输入
        self.add_widget(Label(text='初始化向量 (IV) - 16字节:', size_hint_y=None, height=dp(30)))
        self.iv_input = TextInput(
            text='cdb421d038104126',
            size_hint_y=None,
            height=dp(40),
            hint_text='输入16字节IV'
        )
        self.add_widget(self.iv_input)

        # 按钮区域
        btn_layout = BoxLayout(size_hint_y=None, height=dp(50), spacing=dp(10))
        encrypt_btn = Button(text='加密', background_color=[0.4, 0.5, 0.9, 1])
        encrypt_btn.bind(on_press=self.do_encrypt)
        clear_btn = Button(text='清空', background_color=[0.7, 0.7, 0.7, 1])
        clear_btn.bind(on_press=self.do_clear)
        btn_layout.add_widget(encrypt_btn)
        btn_layout.add_widget(clear_btn)
        self.add_widget(btn_layout)

        # 结果显示
        self.add_widget(Label(text='加密结果:', size_hint_y=None, height=dp(30)))
        self.result_output = TextInput(
            multiline=True,
            size_hint_y=None,
            height=dp(100),
            readonly=True,
            background_color=[0.95, 0.95, 0.95, 1]
        )
        self.add_widget(self.result_output)

        # 复制按钮
        copy_btn = Button(
            text='复制结果',
            size_hint_y=None,
            height=dp(40),
            background_color=[0.3, 0.7, 0.4, 1]
        )
        copy_btn.bind(on_press=self.copy_result)
        self.add_widget(copy_btn)

    def do_encrypt(self, instance):
        """执行加密"""
        plaintext = self.plaintext_input.text
        key = self.key_input.text
        iv = self.iv_input.text

        if not plaintext:
            self.show_popup('错误', '请输入要加密的内容')
            return

        if not key or len(key) != 16:
            self.show_popup('错误', '密钥必须是16字节')
            return

        if not iv or len(iv) != 16:
            self.show_popup('错误', 'IV必须是16字节')
            return

        result, error = AESUtils.encrypt(plaintext, key, iv)
        if error:
            self.show_popup('加密失败', error)
        else:
            self.result_output.text = result
            self.show_popup('成功', '加密成功！')

    def do_clear(self, instance):
        """清空输入"""
        self.plaintext_input.text = ''
        self.result_output.text = ''

    def copy_result(self, instance):
        """复制结果"""
        if self.result_output.text:
            Clipboard.copy(self.result_output.text)
            self.show_popup('成功', '已复制到剪贴板！')

    def show_popup(self, title, message):
        """显示弹出窗口"""
        popup = Popup(
            title=title,
            content=Label(text=message, font_size=dp(16)),
            size_hint=(0.8, 0.3)
        )
        popup.open()


class DecryptTab(BoxLayout):
    """解密标签页"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = dp(10)
        self.spacing = dp(10)

        # 密文输入
        self.add_widget(Label(text='密文 (Base64):', size_hint_y=None, height=dp(30)))
        self.ciphertext_input = TextInput(
            multiline=True,
            size_hint_y=None,
            height=dp(100),
            hint_text='输入要解密的Base64密文'
        )
        self.add_widget(self.ciphertext_input)

        # 密钥输入
        self.add_widget(Label(text='密钥 (Key) - 16字节:', size_hint_y=None, height=dp(30)))
        self.key_input = TextInput(
            text='844dd1be967b6e9e',
            size_hint_y=None,
            height=dp(40),
            hint_text='输入16字节密钥'
        )
        self.add_widget(self.key_input)

        # IV输入
        self.add_widget(Label(text='初始化向量 (IV) - 16字节:', size_hint_y=None, height=dp(30)))
        self.iv_input = TextInput(
            text='cdb421d038104126',
            size_hint_y=None,
            height=dp(40),
            hint_text='输入16字节IV'
        )
        self.add_widget(self.iv_input)

        # 按钮区域
        btn_layout = BoxLayout(size_hint_y=None, height=dp(50), spacing=dp(10))
        decrypt_btn = Button(text='解密', background_color=[0.4, 0.5, 0.9, 1])
        decrypt_btn.bind(on_press=self.do_decrypt)
        clear_btn = Button(text='清空', background_color=[0.7, 0.7, 0.7, 1])
        clear_btn.bind(on_press=self.do_clear)
        btn_layout.add_widget(decrypt_btn)
        btn_layout.add_widget(clear_btn)
        self.add_widget(btn_layout)

        # 结果显示
        self.add_widget(Label(text='解密结果:', size_hint_y=None, height=dp(30)))
        self.result_output = TextInput(
            multiline=True,
            size_hint_y=None,
            height=dp(100),
            readonly=True,
            background_color=[0.95, 0.95, 0.95, 1]
        )
        self.add_widget(self.result_output)

        # 复制按钮
        copy_btn = Button(
            text='复制结果',
            size_hint_y=None,
            height=dp(40),
            background_color=[0.3, 0.7, 0.4, 1]
        )
        copy_btn.bind(on_press=self.copy_result)
        self.add_widget(copy_btn)

    def do_decrypt(self, instance):
        """执行解密"""
        ciphertext = self.ciphertext_input.text
        key = self.key_input.text
        iv = self.iv_input.text

        if not ciphertext:
            self.show_popup('错误', '请输入要解密的密文')
            return

        if not key or len(key) != 16:
            self.show_popup('错误', '密钥必须是16字节')
            return

        if not iv or len(iv) != 16:
            self.show_popup('错误', 'IV必须是16字节')
            return

        result, error = AESUtils.decrypt(ciphertext, key, iv)
        if error:
            self.show_popup('解密失败', error)
        else:
            self.result_output.text = result
            self.show_popup('成功', '解密成功！')

    def do_clear(self, instance):
        """清空输入"""
        self.ciphertext_input.text = ''
        self.result_output.text = ''

    def copy_result(self, instance):
        """复制结果"""
        if self.result_output.text:
            Clipboard.copy(self.result_output.text)
            self.show_popup('成功', '已复制到剪贴板！')

    def show_popup(self, title, message):
        """显示弹出窗口"""
        popup = Popup(
            title=title,
            content=Label(text=message, font_size=dp(16)),
            size_hint=(0.8, 0.3)
        )
        popup.open()


class AESHelperApp(App):
    """AES加密解密应用"""

    def build(self):
        """构建应用界面"""
        # 创建标签面板
        tp = TabbedPanel()
        tp.tab_pos = 'top_left'
        tp.tab_height = dp(50)

        # 加密标签
        encrypt_tab = TabbedPanelItem(text='加密')
        encrypt_tab_content = EncryptTab()
        encrypt_tab.add_widget(encrypt_tab_content)

        # 解密标签
        decrypt_tab = TabbedPanelItem(text='解密')
        decrypt_tab_content = DecryptTab()
        decrypt_tab.add_widget(decrypt_tab_content)

        tp.add_widget(encrypt_tab)
        tp.add_widget(decrypt_tab)

        return tp


if __name__ == '__main__':
    AESHelperApp().run()
