from django.shortcuts import render, redirect

from .forms import SupplierForm



def supplier_view(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data
            # For example, save it to the database or send an email
            # Redirect to a new URL or render a success template
            return redirect('success')
    else:
        form = SupplierForm()
    
    return render(request, 'supplier_new.html', {'form': form})
