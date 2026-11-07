from django.shortcuts import render
from django.http import Http404

COURSES_DATA = [

    {

        'id': 101,

        'code': 'DTI412',

        'title': 'Special Topic in Application Development',

        'credits': 3,

        'instructor': 'Dr. Sirisuda Buathongkeow',

        'description': 'Learn Django, RESTful APIs, JWT security and cloud deployment.'

    },

    {

        'id': 102,

        'code': 'DTI201',

        'title': 'Database Systems & Data Modeling',

        'credits': 3,

        'instructor': 'Department Faculty',

        'description': 'Learn relational databases, ER diagrams, SQL and normalization.'

    },

    {

        'id': 103,

        'code': 'DTI305',

        'title': 'Frontend Web Technologies & React',

        'credits': 3,

        'instructor': 'Department Faculty',

        'description': 'Learn JavaScript, React components and API integration.'

    }

]


def home_view(request):

    context = {

        'total_courses': len(COURSES_DATA),

        'featured_course': COURSES_DATA[0],

    }

    return render(request, 'catalog/home.html', context)


def course_list_view(request):

    return render(request, 'catalog/course_list.html', {

        'courses': COURSES_DATA

    })


def course_detail_view(request, course_id):

    course = next(

        (item for item in COURSES_DATA if item['id'] == course_id),

        None

    )

    if course is None:

        from django.http import Http404

        raise Http404("Course not found")

    return render(request, 'catalog/course_detail.html', {

        'course': course

    })
def inquiry_view(request):
   errors = []
   submitted_data = None
   if request.method == 'POST':
       student_name = request.POST.get('student_name', '').strip()
       email = request.POST.get('email', '').strip()
       course_code = request.POST.get('course_code', '').strip()
       message = request.POST.get('message', '').strip()
       if not student_name:
           errors.append('Student name is required.')
       if not email or '@' not in email:
           errors.append('Please enter a valid email.')
       if not message:
           errors.append('Message is required.')
       if not errors:
           submitted_data = {
               'student_name': student_name,
               'email': email,
               'course_code': course_code,
               'message': message,
           }
   return render(request, 'catalog/inquiry.html', {
       'courses': COURSES_DATA,
       'errors': errors,
       'submitted_data': submitted_data,
   })
 
 
