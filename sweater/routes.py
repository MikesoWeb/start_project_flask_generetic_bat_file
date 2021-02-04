from sweater import app
 
 
@app.route('/')
def index():
   name = 'Mike'
   return f'Hello, {name}'
