from django.shortcuts import render, redirect
from django.contrib import messages
from bug.models import Bug

# View function to add a new bug to the database
def add_bug(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        bug_type = request.POST.get('bug_type')
        status = request.POST.get('status')
        
        # Check if all required fields are provided
        if description and bug_type and status:
            # Create and save the bug to the database
            bug = Bug(description=description, bug_type=bug_type, status=status)
            bug.save()
            messages.success(request, 'Bug added successfully')
            return redirect('all_bugs')
        else:
            # If any required field is missing
            return render(request, 'bug/bug-form.html')

    # Render the bug input form if the request method is not POST
    return render(request, 'bug/bug-form.html')

# View function to display a list of all bugs
def all_bugs(request):
    # Retrieve bug data from the database and order it by the report date
    bug_data = Bug.objects.order_by('-report_date')
    return render(request, "bug/all-bugs.html", {"data": bug_data})

# View function to display the details of a specific bug
def bug_detail(request, id):
    # Retrieve the bug with the specified ID from the database
    bug = Bug.objects.get(id=id)
    return render(request, 'bug/bug-detail.html', {'bug': bug})
