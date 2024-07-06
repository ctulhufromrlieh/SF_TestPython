from django.shortcuts import render, redirect

from .forms import *

# def handle_uploaded_file(file):
#         with open(args[1], 'r') as file:
#             file_content = file.read()
#             words = file_content.split(" ")

def get_word_count_of_file(file, search_word):
    # print("file = ", file)
    # print("type(file)=", type(file))
    with open(file, 'r') as f:
        file_content = f.read()
        words = file_content.split(" ")

        count = 0
        for word in words:
            if (word == search_word):
                count += 1

        return count

def file_form_view(request):
    if request.method == 'POST':
        wf = WordFile.objects.first()
        form = WordFileForm(request.POST, request.FILES, instance=wf)
        if form.is_valid():
            form.save()
            return redirect('search_form')
            # return redirect('file_form')
    else:
        form = WordFileForm()

    return render(request, 'file_form.html', {
        'form': form
    })

def search_form_view(request):
    wf = WordFile.objects.first()
    if request.method == 'POST':
        # wf = WordFile.objects.first()
        form = WordCountForm(request.POST, request.FILES, instance=wf)
        if form.is_valid():
            word_count = get_word_count_of_file('media/' + wf.file.name, wf.search_word)
            wf.word_count=word_count
            form.save()

            return redirect('search_form')
    else:
        form = WordCountForm()

    print("wf.word_count = ", wf.word_count)

    return render(request, 'search_form.html', {
        'form': form,
        'search_word': wf.search_word,
        'word_count': wf.word_count,
    })