from utils import view
from sanic.response import file, HTTPResponse
import os


class IndexView(view.View):

    async def get(self, request, path=""):
        template_dir = request.app.config['TEMPLATE_DIR']
        html_dir = None
        current_path = path.split('/')
        while len(current_path) > 0:
            path = '/'.join(current_path)
            html_dir = os.path.join(template_dir, path, 'index.html')
            if os.path.exists(html_dir):
                break
            else:
                html_dir = os.path.join(template_dir, f'{path}.html')
            if os.path.exists(html_dir):
                break
            else:
                html_dir = os.path.join(template_dir, path)
            if os.path.exists(html_dir):
                break
            current_path.pop(-1)
        if os.path.exists(html_dir):
            return await file(
                html_dir,
                headers={'Content-Type': 'text/html; charset=utf-8'}
            )
        return HTTPResponse(status=404)
