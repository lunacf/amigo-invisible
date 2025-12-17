# Bot de WhatsApp con Selenium

## ⚠️ ADVERTENCIAS IMPORTANTES

- **Riesgo de bloqueo**: WhatsApp puede detectar automatización y bloquear tu cuenta
- **Uso responsable**: No envíes spam ni mensajes no solicitados
- **Términos de servicio**: Esto viola los términos de servicio de WhatsApp
- **Solo para educación**: Usa este código únicamente con fines educativos

## Instalación

1. Instala las dependencias necesarias:
```bash
pip install selenium
```

2. Descarga Edge WebDriver:
   - Visita: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
   - Descarga la versión que coincida con tu Edge
   - Colócalo en la carpeta del proyecto o en tu PATH
   - O deja que Selenium lo descargue automáticamente

## Configuración

Edita el archivo `test.py`:

1. **Números de teléfono**: Agrega los números en formato internacional sin el símbolo `+`
   ```python
   numeros = [
       "541173340825",  # Argentina: 54 + 9 + área + número
       "541134256545",  # México: 52 + 1 + área + número
   ]
   ```

2. **Mensajes**: Personaliza los mensajes aleatorios
   ```python
   mensajes = [
       "Prueba de mensaje automatizado test 1 ",
       "Prueba de mensaje automatizado test 2",
   ]
   ```

## Uso

1. Ejecuta el script:
```bash
python test.py
```

2. Se abrirá Edge con WhatsApp Web
3. Escanea el código QR con tu teléfono
4. El bot comenzará a enviar los mensajes automáticamente

## Características

- ✅ Envío automático de mensajes
- ✅ Mensajes aleatorios desde una lista
- ✅ Delays aleatorios entre mensajes (anti-detección)
- ✅ Múltiples destinatarios
- ✅ Reporte de mensajes exitosos/fallidos

## Limitaciones

- Requiere escanear QR cada vez que se ejecuta
- WhatsApp puede limitar la cantidad de mensajes
- Necesita conexión a internet estable
- El navegador debe permanecer abierto

## Consejos

- Usa delays largos entre mensajes (30-60 segundos es más seguro)
- Limita la cantidad de mensajes por día
- No uses tu número personal principal
- Prueba primero con números de prueba
