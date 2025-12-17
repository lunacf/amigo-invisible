from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import random

class WhatsAppBot:
    def __init__(self, modo_oculto=True):
        opciones = webdriver.EdgeOptions()
        if modo_oculto:
            opciones.add_argument("--start-minimized")
        self.driver = webdriver.Edge(options=opciones)
        self.wait = WebDriverWait(self.driver, 30)
        self.mensajes_enviados = []
        if modo_oculto:
            self.driver.minimize_window()
    
    def encriptar_mensaje(self, mensaje):
        return ''.join(' ' if c == ' ' else '*' for c in mensaje)
    
    def limpiar_numero(self, numero):
        return numero.replace('+', '').replace(' ', '').replace('-', '').replace('(', '').replace(')', '')
    
    def validar_numero(self, numero):
        return numero.isdigit() and 10 <= len(numero) <= 15
        
    def abrir_whatsapp_web(self):
        self.driver.get("https://web.whatsapp.com")
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')))
        time.sleep(2)
        
    def enviar_mensaje(self, numero, mensaje):
        try:
            numero_limpio = self.limpiar_numero(numero)
            if not self.validar_numero(numero_limpio):
                return False
            
            mensaje_encriptado = self.encriptar_mensaje(mensaje)
            print(f"\nEnviando a +{numero_limpio}: {mensaje_encriptado}")
            
            self.driver.get(f"https://web.whatsapp.com/send?phone={numero_limpio}")
            time.sleep(5)
            
            xpaths = [
                '//div[@contenteditable="true"][@data-tab="10"]',
                '//div[@contenteditable="true"][@role="textbox"]',
                '//div[@title="Escribe un mensaje aquí"]',
                '//div[@title="Type a message"]',
                '//footer//div[@contenteditable="true"]',
            ]
            
            cuadro_texto = None
            for xpath in xpaths:
                try:
                    cuadro_texto = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, xpath))
                    )
                    break
                except:
                    continue
            
            if not cuadro_texto:
                return False
                
            time.sleep(2)
            cuadro_texto.click()
            time.sleep(0.5)
            
            for char in mensaje:
                cuadro_texto.send_keys(char)
                time.sleep(0.02)
            
            time.sleep(1)
            cuadro_texto.send_keys(Keys.ENTER)
            time.sleep(2)
            
            self.mensajes_enviados.append({
                'numero': numero_limpio,
                'mensaje': mensaje,
                'encriptado': mensaje_encriptado
            })
            
            time.sleep(random.randint(10, 15))
            return True
            
        except Exception as e:
            print(f"Error: {type(e).__name__}")
            return False
    
    def sortear_amigos_invisibles(self, participantes):
        nombres = list(participantes.values())
        numeros = list(participantes.keys())
        
        for _ in range(100):
            nombres_disponibles = nombres.copy()
            random.shuffle(nombres_disponibles)
            
            valido = True
            sorteo = {}
            for i, numero in enumerate(numeros):
                if participantes[numero] == nombres_disponibles[i]:
                    valido = False
                    break
                sorteo[numero] = f"Tu amigo invisible es: {nombres_disponibles[i]}"
            
            if valido:
                return sorteo
        
        sorteo = {}
        for i, numero in enumerate(numeros):
            siguiente = (i + 1) % len(numeros)
            sorteo[numero] = f"Tu amigo invisible es: {participantes[numeros[siguiente]]}"
        return sorteo
    
    def enviar_mensajes_masivos(self, participantes):
        exitosos = 0
        fallidos = 0
        
        print("\n" + "="*50)
        print("SORTEO DE AMIGO INVISIBLE")
        print("="*50 + "\n")
        
        sorteo = self.sortear_amigos_invisibles(participantes)
        
        for numero, mensaje in sorteo.items():
            if self.enviar_mensaje(numero, mensaje):
                exitosos += 1
            else:
                fallidos += 1
        
        print("\n" + "="*50)
        print("RESULTADOS")
        print("="*50)
        
        if self.mensajes_enviados:
            for i, envio in enumerate(self.mensajes_enviados, 1):
                destinatario = next((n for num, n in participantes.items() 
                                   if self.limpiar_numero(num) == envio['numero']), "?")
                print(f"\n{i}. {destinatario}: {envio['mensaje']}")
        
        print(f"\n{exitosos} enviados, {fallidos} fallidos")
        print("="*50)
    
    def cerrar(self):
        self.driver.quit()


participantes = {
    # Aca se agregan los numeros y nombres de los participantes
    # Formato: "numero": "nombre"
    # Ejemplos:
    # "5491123456789": "Juan",      
    # "5491187654321": "María",
    # "5215512345678": "Pedro",     
    # "573001234567": "Ana",        
}

if __name__ == "__main__":
    MODO_OCULTO = False
    bot = WhatsAppBot(modo_oculto=MODO_OCULTO)
    
    try:
        bot.abrir_whatsapp_web()
        if MODO_OCULTO:
            input("Escanea el QR y presiona Enter...")
        bot.enviar_mensajes_masivos(participantes)
    except KeyboardInterrupt:
        print("\nInterrumpido")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        input("\nPresioná Enter para cerrar...")
        bot.cerrar()
