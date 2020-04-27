import os
import os.path

import cherrypy
import cherrypy_cors

localDir = os.path.dirname(__file__)
absDir = os.path.join(os.getcwd(), localDir)

class ModelServe(object):

    @cherrypy.expose
    def index(self):
        return "Good bye!"

    @cherrypy.expose
    def get_model_results(self):

        if cherrypy.request.method == 'OPTIONS':
            cherrypy_cors.preflight(allowed_methods=['GET', 'POST'])
            return ''

        full_file_name = os.path.join(absDir, 'model.txt')
        file_content = open(full_file_name).read()

        cherrypy.response.headers['Access-Control-Allow-Origin'] = '*'
        return file_content

if __name__ == '__main__':
    cherrypy_cors.install()
    cherrypy.config.update({
        'server.socket_host': '127.0.0.1',
        'server.socket_port': 8080,
        'cors.expose.on': True,
    })
    cherrypy.quickstart(ModelServe())