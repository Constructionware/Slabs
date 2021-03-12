# slabs/start.py

from Application.mainserver import gco, slabs

@slabs.route('/')
async def mainin(req, res):
    res.media = {'message': "OK"}

if __name__ == '__main__':    
    print(f"{gco.TITLE} Web Application Server Starting on PORT: {gco.PORT}")
    slabs.run(
        host=gco.HOST,
        port=gco.PORT,
        debug=gco.DEBUG,
        limit_concurrency=gco.CONNECTIONS,
        limit_max_requests=gco.MAX_REQUESTS,
        loop=gco.LOOP,
        access_log=gco.ACCESS_LOG 
    )

