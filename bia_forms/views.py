from django.shortcuts import render, redirect, get_object_or_404
from django.forms.models import model_to_dict
from .models import SignalLog, Agent, Artifact
from .forms import AgentRecruitmentForm, ArtifactModelForm

# Create your views here.
def signal_log_view(request):
    success_msg = None
    
    if request.method == 'POST':
        # 1 Daten manuell aus dem request.POST Dictionary holen (alles Strings)
        freq_str = request.POST.get('frequency')
        sig_type = request.POST.get('signal_type')
        intens_str = request.POST.get('intensity')
        date_str = request.POST.get('received_date')
        message = request.POST.get('decoded_message')
        
        req_dict = request.POST
        
        # Manuelle Konvertierung und Speicherung
        try:
            SignalLog.objects.create(
                frequency=float(freq_str),
                signal_type=sig_type,
                intensity=int(intens_str),
                received_date=date_str,
                decoded_message=message
            )
            return redirect('start:index')
            success_msg = f"Signal auf {freq_str} MHz erfolgreich in Datenbank gespeichert."
        except ValueError:
            success_msg = "FEHLER: Ungültige Datenformate erhalten."
        
    return render(request, 'bia_forms/app1.html', {'success_msg': success_msg})


# --- VIEW 2: Django Form API ---
def agent_recruit_view(request):
    success_msg = None
    
    if request.method == 'POST':
        form = AgentRecruitmentForm(request.POST)
        
        # Django validiert für uns (Datentypen, Pflichtfelder etc.)
        if form.is_valid():
            # data ist ein sauberes Dictionary (cleaned_data)
            # Da unsere Form-Feldnamen exakt den Model-Feldnamen entsprechen,
            # können wir Dictionary-Unpacking (**) nutzen!
            
            #---------------------
            # way(s) ohne redirect
            #---------------------
            
            # way 1 (wenn Model-Feldnamen und Form-Feldnamen identisch sind)
            # Agent.objects.create(**form.cleaned_data)
            
            # way 2 (wenn Model-Felnamen und Form-Feldnamen sich unterscheiden)
            # Agent.objects.create(
            #     full_name=form.cleaned_data['full_name'],
            #     email=form.cleanded_data.get('email'),
            #     ...
            # )
            #success_msg = "ich bin erfolgreich übergeben worden"
            
            #--------------------------------------------
            # Wenn redirect benützt wird zu success Seite
            #--------------------------------------------
            agent = Agent(**form.cleaned_data)
            agent.save()
            
            return redirect('bia_forms:agent-confirm', agent.id)
            #return agent_confirm_view(request, agent.id)
    
    form = AgentRecruitmentForm()
    
    return render(request, 'bia_forms/app2.html', {
        'success_msg': success_msg,
        'form': form
    })
    
def agent_confirm_view(request, id):
    agent = get_object_or_404(Agent, pk=id)
    return render(request, 'bia_forms/agent_success.html', {'agent': agent})

# --- LIST VIEW: Alle Agenten ---
def agent_list_view(request):
    agents = Agent.objects.all().order_by('-years_of_experience')
    return render(request, 'bia_forms/agents_list.html', {'agents': agents})

# --- DETAIL VIEW: Einzelner Agent ---
def agent_detail_view(request, pk):
    agent = get_object_or_404(Agent, pk=pk)
    return render(request, 'bia_forms/agent_detail.html', {'agent': agent})

# --- UPDATE VIEW: Agent bearbeiten ---
def agent_edit_view(request, pk):
    # 1. Das existierende Objekt aus der Datenbank holen
    agent = get_object_or_404(Agent, pk=pk)

    if request.method == 'POST':
        # Daten aus dem Request in das Formular laden
        form = AgentRecruitmentForm(request.POST)
        
        if form.is_valid():            
            # Wir holen die sauberen Daten
            data = form.cleaned_data
            
            # Wir überschreiben die Werte des Agenten-Objekts
            agent.full_name = data['full_name']
            agent.email = data['email']
            agent.codename = data['codename']
            agent.years_of_experience = data['years_of_experience']
            agent.special_skills = data['special_skills']
            agent.agrees_to_memory_wipe = data['agrees_to_memory_wipe']
            
            # Speichern in der DB
            agent.save()
            
            # Weiterleitung zur Detailansicht oder Liste
            return redirect('bia_forms:agent-detail', pk=agent.pk)
            
    else:
        # GET Request: Formular initialisieren
        
        # OPTION A: Manuelles Mapping 
        # initial_data = {
        #     'full_name': agent.full_name,
        #     'email': agent.email,
        #     'codename': agent.codename,
        #     ...
        # }

        # OPTION B: Der Profi-Weg mit model_to_dict (Empfohlen)
        # Wandelt das Model-Objekt automatisch in ein Dictionary um
        initial_data = model_to_dict(agent)
        
        # Wir übergeben die Daten an 'initial'
        form = AgentRecruitmentForm(initial=initial_data)

    # Wir nutzen dein existierendes Template (app2.html), 
    # geben aber einen anderen Titel mit, damit der User sieht, dass er editiert.
    context = {
        'form': form,
        'heading': f"Akte bearbeiten: {agent.get_codename_display()}",
        'btn_text': "ÄNDERUNGEN SPEICHERN" # Optional für den Button
    }
    
    # Hier nutzen wir wieder dein existierendes Formular-Template
    return render(request, 'bia_forms/app2.html', context)

# --- DELETE VIEW: Agent löschen ---
def agent_delete_view(request, pk):
    agent = get_object_or_404(Agent, pk=pk)
    
    if request.method == 'POST':
        agent.delete()
        return redirect('bia_forms:agent-list')
    
    # Sicherheitsabfrage Template
    return render(request, 'bia_forms/agent_confirm_delete.html', {'agent': agent})


# --- VIEW 3: ModelForm ---
def artifact_create_view(request):
    success_msg = None
    
    if request.method == 'POST':
        form = ArtifactModelForm(request.POST)
        if form.is_valid():
            print(f"HALLO, HIER IST DIE RÜCKGABE: {form.save()}")
            success_msg = "Artefakt erfolgreich katalogisiert und weggesperrt"
            form = ArtifactModelForm()
    else:
        form = ArtifactModelForm()
    
    return render(request, 'bia_forms/app3.html', {
        'success_msg': success_msg,
        'form': form
    })
    
# --- Erklärung wie Django zu den einzelnen Daten in der Datenbank kommt ---
def artifacts_list(request):
    artifacts = Artifact.objects.values()
    
    return render(request, 'bia_forms/artifacts_list.html', {'artifacts': artifacts})

# Edit Artefakt Objekte
def artifact_edit(request, id):
    artifact = get_object_or_404(Artifact, pk=id)
    
    if request.method == 'POST':
        # Das sagt Django: "Nimm diese neuen Daten (request.POST) und überschreibe DIESES Objekt (artifact) damit"
        form = ArtifactModelForm(request.POST, instance=artifact)
        
        if form.is_valid():
            form.save()
            return redirect('bia_forms:artifacts-list')
    
    form = ArtifactModelForm(instance=artifact)
    
    return render(request, 'bia_forms/artifact_edit.html', {
        'form': form,
        'artifact': artifact
    })
  
        