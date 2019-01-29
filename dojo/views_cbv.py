from django.http import HttpResponse, JsonResponse
from django.views.generic import View, TemplateView
import os

class PostList1(View):
    def get(self,request):
        name = '유승룡'
        html = self.get_template_string().format(name = name)
        return HttpResponse(html)

    def get_template_string(self):
        return '''
            <h1>안녕하세요</h1>
            <p>{name}</p>
        '''

post_list1 = PostList1.as_view()

class PostList2(TemplateView):
    template_name = 'dojo/post_list2.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['name'] = '유승룡'
        return context

post_list2 = PostList2.as_view()

class PostList3(View):
    def get(self,request):
        return JsonResponse(self.get_data(),json_dumps_params={'ensure_ascii':False})

    def get_data(self):
        return {
            'message':'안녕하세요',
            'items':['python','django','AWS','Azure','Celery']
        }

post_list3 = PostList3.as_view()

class ExcelDown(View):
    filepath = '/Users/ryong/Downloads/test.xlsx'
    def get(self,request):
        filename = os.path.basename(self.filepath)
        with open(self.filepath, 'rb') as f:
            response = HttpResponse(f, content_type='application/vnd.ms-excel')
            response['content-disposition']='attachment;filename = "{}"'.format(filename)
        return response

excel_downloader = ExcelDown.as_view()