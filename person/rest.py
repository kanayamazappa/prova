# -*- coding: utf-8 -*-
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from models import Person
from serializer import PersonSerializer
import facebook, hashlib, hmac, requests

def genAppSecretProof(app_secret, access_token):
    h = hmac.new (
        app_secret.encode('utf-8'),
        msg=access_token.encode('utf-8'),
        digestmod=hashlib.sha256
    )
    return h.hexdigest()

@api_view(['GET','POST','DELETE'])
def PersonRest(request, _facebookid=False):
    if request.method == 'GET':
        limit = request.query_params.get('limit', False)
        
        data = []
        
        lista = Person.objects.all()
        
        if limit:
            lista = lista[:int(limit)]
        
        for item in lista:
          data.append({
              'facebookId': item.facebookId,
              'name': item.name,
              'gender': item.gender,
              'link': item.link,
          })
        return Response(data=data, status=200)
    elif request.method == 'POST':
        facebookId = request.data.get('facebookId', False)
        
        app_id = '630037973709463'
        secret_id = '9993ea6366aac8a164426445820e4cb8'
        try:
            access_token = facebook.get_app_access_token(app_id, secret_id)
        except:
            return Response(data={'status': 404, 'message': u'Não foi possível obter o access token do Facebook.'}, status=404)
        
        try:
            graph = facebook.GraphAPI(access_token)
        except:
            return Response(data={'status': 404, 'message': u'Access token inválido.'}, status=404)
        
        try:
            appsecret_proof = genAppSecretProof(secret_id, access_token)
        except:
            return Response(data={'status': 404, 'message': u'Não foi possível gerar o appsecret_proof.'}, status=404)
        
        try:
            profile = graph.get_object(facebookId, fields=['id', 'name', 'gender', 'link', 'first_name'], appsecret_proof=appsecret_proof)
        except:
            return Response(data={'status': 404, 'message': u'Não foi possível obter o profile do usuário.'}, status=404)
        
        '''
        
        ------------------------
        Problemas com o Facebook
        ------------------------
        
        A propriedade USERNAME foi removida por isso utilizei o link (https://developers.facebook.com/docs/apps/upgrading#upgrading_v2_0_graph_api).
        A propriedate GENDER precisa que o usuario estaja logado com a conta do profile pesquisado ou seja amigo ou de permissão para o APP para ter o acesso 
        (https://developers.facebook.com/docs/facebook-login/permissions?locale=pt_BR#reference-public_profile). Como no e-mail me altorizaram a usar a imaginação encontrei a API
        genderize.io (https://genderize.io/) que retorna o genero pelo primeiro nome da pessoa.
        
        Observação: a propriedade appsecret_proof esta sendo passada como recomendação da documentação do Facebook porém ainda não está trazendo o sexo do perfil pesquisado.
        
        '''
        
        if "gender" in profile:
            gender = profile["gender"]
        else:
            try:
                url = "https://api.genderize.io/?name=%s" % profile['first_name']
                ret = requests.get(url).json()
                gender = ret['gender']
            except:
                gender = None
        
        person = Person(
            facebookId=profile["id"],
            name=profile["name"],
            link=profile["link"],
            gender=gender,
        )
        person.save()
        
        data = {
            'status': 201,
            'person': {
                'facebookId': person.facebookId,
                'name': person.name,
                'link': person.link,
                'gender': person.gender,
            },
        }
        
        return Response(data=data, status=201)
        
    elif request.method == 'DELETE':
        Person.objects.filter(facebookId=_facebookid).delete()
        return Response(status=204)
    else:
        return Response(data={'status': 404, 'message': u'Operação inválida'}, status=404)
    