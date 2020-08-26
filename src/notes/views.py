from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from .forms import NoteModelForm


def note_list_view(request):
    form = NoteModelForm
    if request.method == "POST":
        form = NoteModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("main_list")

    to_do_list = Note.objects.filter(finished=False)
    finished_list = Note.objects.filter(finished=True)
    context = {'to_do_list': to_do_list,
               'finished_list': finished_list,
               "form": form}
    return render(request, "note_list.html", context)


def done_item(request, id):
    note = get_object_or_404(Note, id=id)
    note.finished = True
    note.save()
    return redirect('main_list')


def delete_item(request, id):
    note = get_object_or_404(Note, id=id)
    note.delete()
    return redirect('main_list')


def recover_item(request, id):
    note = get_object_or_404(Note, id=id)
    note.finished = False
    note.save()
    return redirect('main_list')
