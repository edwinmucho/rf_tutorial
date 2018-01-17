from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


snippet = Snippet(code='foo = "bar"\n')
snippet.save()

snippet = Snippet(code='print("Hello, world")\n')
snippet.save()

serializer = SnippetSerializer(snippet)
serializer.data
######################################
# ReturnDict([('id', 2),
#             ('title', ''),
#             ('code', 'print("Hello, world")\n'),
#             ('linenos', False),
#             ('language', 'python'),
#             ('style', 'friendly')])
#######################################
content = JSONRenderer().render(serializer.data)
content
#b'{"id":2,"title":"","code":"print(\\"Hello, world\\")\\n","linenos":false,"language":"python","style":"friendly"}'


from django.utils.six import BytesIO

stream = BytesIO(content)
data = JSONParser().parse(stream)
#########################################
# {'code': 'print("Hello, world")\n',
#  'id': 2,
#  'language': 'python',
#  'linenos': False,
#  'style': 'friendly',
#  'title': ''}
#########################################

serializer = SnippetSerializer(data=data)
serializer.is_valid()
# True
serializer.save()
# <Snippet: Snippet object (3)>

serializer = SnippetSerializer(Snippet.objects.all(), many=True)
serializer.data
##########################################
# [OrderedDict([('id', 1), ('title', ''), ('code', 'foo = "bar"\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')]),
# OrderedDict([('id', 2), ('title', ''), ('code', 'print("Hello, world")\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')]),
# OrderedDict([('id', 3), ('title', ''), ('code', 'print("Hello, world")'), ('linenos', False), ('language', 'python'), ('style', 'friendly')])]
##########################################