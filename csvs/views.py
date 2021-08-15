from django.shortcuts import render, redirect
from .forms import CsvUploadForm
from teacherProfile.models import Profile, Subject
from .models import Csv
import csv
from django_pandas.io import read_frame
from django.contrib import messages
# import the logging library
import logging

def Uploader(request):
    if request.method =="GET":
        form = CsvUploadForm()
        return render(request, 'csvs/uploader.html', {'form': form})
    
    
    try:
        csv_file = request.FILES["file_name"]
         
        if not csv_file.name.endswith('.csv'):
            messages.error(request,'File is not CSV type')
            return redirect('uploader')
        #if file is too large, return
        if csv_file.multiple_chunks():
            messages.error(request,"Uploaded file is too big (%.2f MB)." % (csv_file.size/(1000*1000),))
            return redirect('uploader')
        file_data = csv_file.read().decode("utf-8")

        lines = file_data.split("\n")
        
        for line in lines:
            fields = line.split(",") 
            data_dict = {}
            data_dict["first_name"] = fields[0]
            data_dict["last_name"] = fields[1]
            data_dict["email"] = fields[3]
            data_dict["room_number"] = fields[4]
            data_dict["phone_number"] = fields[5]
            data_dict["subjects"] = fields[6]            
            print(data_dict)
            
            
            try:
                form = CsvUploadForm(data_dict)
                if form.is_valid():
                    form.save()
                else:
                    logging.getLogger("error_logger").error(form.errors.as_json())                                                
            except Exception as e:
                logging.getLogger("error_logger").error(form.errors.as_json())                    
                pass

    except Exception as e:
        logging.getLogger("error_logger").error("Unable to upload file. "+repr(e))
        messages.error(request,"Unable to upload file. "+repr(e))
    return redirect('uploader')

    # if request.method == 'POST':
    #     form = CsvUploadForm(request.POST or None, request.FILES or None) 
    #     if form.is_valid():
    #         form.save()
    #     obj = Csv.objects.get(activate=False)
        
    #     with open(obj.file_name.path, 'r') as f:
    #         df = read_frame('test.txt')

    #         df.to_json('data.json')
    #         reader = csv.reader(f) 
            
    #         for i, row in enumerate(reader): 
    #             if i==0:
    #                 pass
    #             else:
    #                 row = "".join(row)
    #                 row = row.replace(";"," ")
    #                 row = row.split()
                    
    #                 #subjects = Subject.objects.get(subject_name=row[0])
    #                 Profile.objects.create(
    #                     first_name =row[0],
    #                     last_name  =row[1],
    #                     email=row[3],
    #                     phone_number=row[4],
    #                     room_number=row[5],
    #                     #subjects =subjects,
    #                 )
    #         obj.activate=True
    #         obj.save
    #         return redirect('')
            
    
   

        
    

    # @method_decorator(login_required)
    # def get(self, request, *args, **kwargs):
    #     form = ImageUploadForm()
    #     return render(request, self.template_name, {'form': form})

    # @method_decorator(login_required)
    # def post(self, request, *args, **kwargs):
    #     form = ImageUploadForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         #images_zip_file = request.FILES['zip']
    #         csv_file = request.FILES['csv']
    #         teacher_details = pd.read_csv(csv_file, delimiter=',')
    #         n_rows = len(teacher_details)
    #         teacher_details = teacher_details.dropna(subset=['First Name', 'Email Address'], how='any')
    #         removed_rows = n_rows - len(teacher_details)

    #         images_zip_file = zipfile.ZipFile(images_zip_file, 'r')
    #         image_name_list = images_zip_file.namelist()

    #         duplicate_rows = 0
    #         for index, teacher in teacher_details.iterrows():
    #             email_id = teacher['Email Address'].strip()
    #             if email_id:
    #                 if Profile.objects.filter(email__iexact=email_id).exists():
    #                     duplicate_rows = duplicate_rows + 1
    #                     continue
    #             profile = Profile()
    #             profile.first_name = teacher['First Name'].strip()
    #             profile.last_name = teacher['Last Name'].strip()
    #             profile.email = email_id
    #             profile.phone_number = teacher['Phone Number'].strip()
    #             profile.room_number = teacher['Room Number'].strip()
    #             profile.save()
    #             subjects = teacher['Subjects taught'].strip().split(',')
    #             if len(subjects) > 5:
    #                 subjects = subjects[:5]
    #             for subject in subjects:
    #                 subject = subject.strip().lower()
    #                 if subjects != '':
    #                     subject, created = Subject.objects.get_or_create(subject_name=subject)
    #                     profile.subjects.add(subject)
    #             image_name = teacher['Profile picture'].strip()
    #             if image_name in image_name_list:
    #                 image = images_zip_file.open(image_name, 'r')
    #                 img = File(image)
    #                 profile.image_name.save(image_name, img, save=True)
    #                 image.close()
    #         images_zip_file.close()
    #         success_rows = n_rows - removed_rows - duplicate_rows
    #         if success_rows > 0:
    #             messages.success(request, str(success_rows) + ' profiles added successfully.')
    #         if removed_rows > 0:
    #             messages.success(request, str(removed_rows) + ' profiles details are incomplete.')
    #         if duplicate_rows > 0:
    #             messages.success(request, str(duplicate_rows) + ' profiles are existing.')
        #return render(request, 'profile/uploader.html', {'form': form})


