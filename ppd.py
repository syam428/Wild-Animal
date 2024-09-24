from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Create a PDF canvas
pdf_file = 'HR_Recruiter_Flowchart.pdf'
c = canvas.Canvas(pdf_file, pagesize=letter)
width, height = letter

# Define positions and sizes
x = 100
y_start = height - 100
box_width = 200
box_height = 50
line_space = 120

# Define the flowchart data
steps = [
    "HR Recruiter Website (Main System)",
    "Technical Support\n- User Assistance\n- Support Tickets\n- Live Chat Support",
    "Bug Fixing & Issue Resolution\n- Monitoring & Debugging\n- Bug Fix & Patch Deployment\n- Regression Testing",
    "Server & Website Maintenance\n- Uptime Monitoring\n- Server Health Checks\n- Load Balancing",
    "Data Backup & Security\n- Database Backups\n- Security Monitoring\n- User Authentication",
    "User Account Management\n- New User Onboarding\n- Account Support\n- Inactivity Monitoring",
    "Feature Updates & Improvements\n- New Feature Rollouts\n- UX Testing & Feedback",
    "Performance Optimization\n- System Performance Monitoring\n- Speed Optimization\n- Scalability Planning"
]

# Draw the flowchart
for i, step in enumerate(steps):
    y = y_start - (i * line_space)
    
    # Draw the box
    c.setFillColor(colors.lightblue)
    c.rect(x, y, box_width, box_height, fill=1)
    
    # Add text
    c.setFillColor(colors.black)
    c.drawString(x + 10, y + box_height - 20, step)
    
    # Draw lines between boxes
    if i > 0:
        c.line(x + box_width/2, y_start - ((i - 1) * line_space), x + box_width/2, y + box_height)

# Save the PDF
c.save()
