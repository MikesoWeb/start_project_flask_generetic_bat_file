from sweater.routes import app
 
 
# Удалите эту строку, если будете использовать консоль 
app.run(port=5050, debug=True)
 
 
# Запустите файл set.bat чтобы записать виртуальные переменные
# FLASK_APP=start.py и FLASK_DEBUG=1 и запускать проект командой flask run
