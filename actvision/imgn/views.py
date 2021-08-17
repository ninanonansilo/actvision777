from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from settings.update_json import *
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from imgn.make_timetable import *
from PIL import ImageColor
# Create your views here.

def imgn(request):
    return render(request,'image.html')


@csrf_exempt
def upload_img(request):
    print("호출 성공")
    if request.method == 'POST':
        if request.is_ajax():
            img = request.FILES.get('chooseFile')  # 이미지를 request에서 받아옴
            path = default_storage.save(user_id +"/img.jpg", ContentFile(img.read()))
            now_kst = time_now()
            UPLOAD("ynu-mcl-act", user_id + "/img.jpg", user_id + "/MEDIA" + now_kst.strftime("/%Y%m%d%H%M%S"))
            os.remove(user_id+"/img.jpg") # 장고에서 중복된 이름의 파일에는 임의로 이름을 변경하기 때문에 임시파일은 제거
            return redirect('image.html')
    else:
        print("POST 호출 실패!")
        return redirect('image.html')

@csrf_exempt
def save_letter(request): # 문자 설정 -> 확인 버튼 눌렀을 시
    if request != "":
        print("========= 시작 ===========")
        print("요청 방식 = " + request.method)
        print(request.body)
        return redirect('image.html')
    else:
        return redirect('image.html')


@csrf_exempt
def event_trans(request):
        #change = request_body_list_text(request.body)
        #data = make_Timetable_text()
        #print(change)
        #now_kst = time_now_local()  # 현재시간 받아옴
        #now_kst1 = time_now()
        #now_kst += 5

        #data["1"]["detail_info"]["x"] = str(change[1])
        #data["1"]["detail_info"]["y"] = str(change[2])
        #data["1"]["detail_info"]["width"] = str(change[3])
        #data["1"]["detail_info"]["height"] = str(change[4])
        ##data["5"]["detail_info"]["scroll_fix"] =
        #data["1"]["detail_info"]["play_speed"] = str(change[5])
        #data["1"]["detail_info"]["play_count"] = str(change[6])
        ##data["5"]["detail_info"]["play_second"] =
        #data["1"]["detail_info"]["font_size"] = "64"     # 폰트사이즈 - 인터페이스 수정 전까지 고정시킴

        #data["1"]["title"] = str(change[0])
        #hex = str("#" + change[8])
        #rgb_value = ImageColor.getcolor(hex,"RGB")
        #data["1"]["detail_info"]["red_green_blue"] = str(rgb_value)

        #data["1"]["time"]["year"] = str(time.localtime(now_kst).tm_year)
        #data["1"]["time"]["month"] = str(time.localtime(now_kst).tm_mon)
        #data["1"]["time"]["day"] = str(time.localtime(now_kst).tm_mday)
        #data["1"]["time"]["hour"] = str(time.localtime(now_kst).tm_hour)
        #data["1"]["time"]["minute"] = str(time.localtime(now_kst).tm_min)
        #data["1"]["time"]["second"] = str(time.localtime(now_kst).tm_sec)

        #createDirectory(user_id)
        #save_file(data)
        #UPLOAD("ynu-mcl-act", user_id+"/send" , user_id + "/JSON/TIMETABLE" + now_kst1.strftime("/%Y%m%d%H%M%S"))

        print("========= 종료 ===========")
        return redirect('image.html')

