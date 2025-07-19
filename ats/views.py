from django.shortcuts import render
from .forms import CandidateForm
from django.shortcuts import redirect

def upload_resume(request):
    if request.method == 'POST':
        form = CandidateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'thank_you.html')
    else:
        form = CandidateForm()
    return render(request, 'upload.html', {'form': form})
def home_redirect(request):
    return redirect('upload_resume')

