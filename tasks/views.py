# Vistas basadas en clases
from django.views.generic.list import ListView  # Lectura del modelo
from django.views.generic.detail import DetailView  # Lectura de un id del modelo
from django.views.generic.edit import CreateView  # crear formularios
from django.views.generic.edit import UpdateView  # Para actualizar campos
# Para eliminar datos del formulario
from django.views.generic.edit import DeleteView

# modelos
from .models import Task
from .forms import FormsTask

# Estos son los import para requerir que sea miembro del staff para crear,editar,borrar
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator


from django.urls import reverse_lazy

# Create your views here.


class TasksViews(ListView):

    model = Task


class TaskDetail(DetailView):
    model = Task


@method_decorator(staff_member_required, name="dispatch")
class TaskCreateViews(CreateView):
    model = Task
    form_class = FormsTask
    success_url = reverse_lazy('tasks')


@method_decorator(staff_member_required, name="dispatch")
class TaskUpdateViews(UpdateView):
    model = Task
    form_class = FormsTask
    template_name_suffix = '_update_form'

    def get_success_url(self) -> str:
        return reverse_lazy('update', args=[self.object.id]) + '?ok'


@method_decorator(staff_member_required, name="dispatch")
class TaskDeleteViews(DeleteView):
    model = Task
    success_url = reverse_lazy('tasks')
