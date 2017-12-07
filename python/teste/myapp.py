from celery import Celery
 
app = Celery(
    'myapp',
    broker='redis://localhost',
    backend='redis'
)
 
@app.task(ignore_result=True)
def print_hello():
    print ('olá celery')
    return ('nao passa nada para o backend')
 
@app.task
def numeros_primos(x):
    multiples = []
    results = []
    for i in xrange(2, x+1):
        if i not in multiples:
            results.append(i)
            for j in xrange(i*i, x+1, i):
                multiples.append(j)
    return results
 
@app.task
def add(x, y):
    return x + y
 
if __name__ == '__main__':
    app.start()
