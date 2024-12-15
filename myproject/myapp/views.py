from django.shortcuts import render,redirect

from rest_framework.decorators import api_view  
from rest_framework.response import Response
from rest_framework import status
from .models import Items
from .serializers import ItemSerializer

@api_view(['GET'])
def get(request):
    items = Items.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def post(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Items
from .serializers import ItemSerializer

@api_view(['GET', 'POST'])
def ins(request):
    if request.method == 'GET':
       
        items = Items.objects.all()
        serializer = ItemSerializer(items, many=True)
        return render(request, 'myapp/home.html', {'items': serializer.data})

    if request.method == 'POST':
        action=request.POST.get('action')
        if action=='Create' :
            form_data = {
                'name': request.POST.get('txt1'),
                'description': request.POST.get('txt2'),
                'price': request.POST.get('txt3'),
            } 
            serializer = ItemSerializer(data=form_data)
            if serializer.is_valid():
                serializer.save()   
                items = Items.objects.all()
                serializer = ItemSerializer(items, many=True)
                return render(request, 'myapp/home.html', {'data': "Item inserted", 'items': serializer.data})
            return render(request, 'myapp/home.html', {'data': "Error inserting item", 'items': []})
        
        elif action=='Update':
            item=Items.objects.get(name=request.POST.get('txt4'))
            item.description=request.POST.get('txt5')   
            item.price=request.POST.get('txt6')
            item.save()
            item=Items.objects.all()
            serializer=ItemSerializer(item,many=True)
            return render(request,'myapp/home.html',{'data':"Updated",'items':serializer.data})
            
        elif action=='Delete':
            item=Items.objects.filter(name=request.POST.get('txt7'))
            item.delete()
            item=Items.objects.all()
            serializer=ItemSerializer(item,many=True)
            return render(request,"myapp/home.html",{'data':"Item deleted","items":serializer.data})




    
    



