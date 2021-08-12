from django.shortcuts import render, redirect
from .forms import CsvUploadForm
from teacherProfile.models import Profile, Subject
from .models import Csv
import csv



def Uploader(request):
    form = CsvUploadForm(request.POST or None, request.FILES or None)
    
    if form.is_valid():
        form.save
        form = CsvUploadForm()
        obj = Csv.objects.get(activate=False)
        print(obj)
        
        with open(obj.file_name.path, 'r') as f:
            reader = csv.reader(f)
            print(reader)
            
            for i, row in enumerate(reader): 
                if i==0:
                    pass
                else:
                    row = "".join(row)
                    row = row.replace(";"," ")
                    row = row.split()
                    print(row)
                    first_name =row[0]
                    last_name  =row[1]
                    email=row[3]
                    phone_number=row[4]
                    room_number=row[5]
                    
                    subjects = Subject.objects.get(subject_name=row[6])
                    Profile.objects.create(
                        first_name=first_name,
                        last_name=last_name,
                        email=email,
                        phone_number=phone_number,
                        room_number=room_number,
                        subjects =subjects,
                    )
            obj.activate=True
            obj.save
            return redirect('')
        
    return render(request, 'csvs/uploader.html', {'form': form})

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


