@echo off
:: Verifica si el archivo requirements.txt existe
if not exist "requirements.txt" (
    echo El archivo requirements.txt no se encuentra en el directorio actual.
    pause
    exit /b 1
)

:: Instala las dependencias listadas en requirements.txt
echo Instalando dependencias desde requirements.txt...
pip install -r requirements.txt

:: Verifica el código de salida de pip
if %ERRORLEVEL% neq 0 (
    echo Ocurrió un error al instalar las dependencias.
    pause
    exit /b 1
)

echo Todas las dependencias se han instalado correctamente.
pause
exit /b 0