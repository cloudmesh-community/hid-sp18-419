from eve import Eve
from disk import Disk
import platform
import psutil
import json
from hurry.filesize import size
from flask import Response

app = Eve()

@app.route('/disk', methods=['GET'])
def get_disk_info():    
    du = psutil.disk_usage('/')
    pct_str = str(du.percent) + '%'
    disk = Disk(platform.platform(), size(du.total), size(du.used),
                    size(du.free), pct_str)

    sdata = json.dumps(disk.__dict__)

    response = Response()
    response.headers["status"] = 200
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    response.data = sdata
    
    return response

if __name__ == "__main__":
    app.run()
