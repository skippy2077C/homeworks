from django.shortcuts import render
# renderni chaqirib olamiz 
# Create your views here.
pupils_info = {
        1 : {"id": 1, "name": "Inomjon Qurbonov", 1: [2, 4, 1], 2: [5, 10, 5], 3: [5, 5],"jami":37},
        2 : {"id": 2, "name": "Muhammadyusuf Abduvaliyev", 1: [3, 5, 2], 2: [4, 10, 4], 3: [5, 3], "jami":36},
        3 : {"id": 3, "name": "Shohruhbek Turdaliyev", 1: [3, 0, 2], 2: [3, 10, 3], 3: [5, 3], "jami":29},
        4 : {"id": 4, "name": "Zafarbek Olimboyev", 1: [3, 5, 2], 2: [5, 10, 4], 3: [5, 5], "jami":39},
        5 : {"id": 5, "name": "Samariddin Baxtiyorov", 1: [2, 5, 2], 2: [3, 10, 1], 3: [5, 3], "jami":31},
    }
# ro'yxatni lug'at shaklida tuzib olamiz     
mezonlar = {1 : [3, 5, 2 ], 2 : [5, 10, 5], 3:[5, 5]}
# mezonlarni tuzib olamiz 

def pupils(request):
    global pupils_info
    global mezonlar
    return render(request,template_name='pupils.html',context={'mezonlar':mezonlar,"info": pupils_info})

def pupil_info(request,id):
    global pupils_info
    global mezonlar
    return render(request,template_name='pupil_info.html',context={'mezonlar':mezonlar,"info": pupils_info.get(id)})
