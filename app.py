from reportlab.pdfgen import canvas
import datetime

def pdf_gen():
  datatime = ''.join(str(datetime.datetime.now()).split(' ')).replace(':','-')

  c = canvas.Canvas('./%s.pdf' % datatime)
  c.drawString(100,750, 'Selected Payment Option: ')
  c.drawString(100,730, 'Sample data')

  # canvas.line
  # 1st digit is margin left
  # 2nd digit is vertical position of left tip
  # 3rd digit is margin right
  # 4th digit is vertical position of right tip
  c.line(1,744,747,744)
  c.save()

  return c

pdf_gen()