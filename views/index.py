from utils import view
from sanic.response import file
import os


class IndexView(view.View):

    async def get(self, request, path=""):
        template_dir = request.app.config['TEMPLATE_DIR']
        html_dir = os.path.join(template_dir, path, 'index.html')
        if not os.path.exists(html_dir):
            html_dir = os.path.join(template_dir, f'{path}.html')
        return await file(
            html_dir,
            headers={'Content-Type': 'text/html; charset=utf-8'}
        )
