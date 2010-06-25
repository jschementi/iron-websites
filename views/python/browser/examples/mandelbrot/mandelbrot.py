import sys
sys.path.append("bin")

# Uses C# for the actual mandelbrot calculation, because it's
# very very number crunchy. However, that doesn't mean IronPython is
# slow, in-fact, on mandelbrot IronPython it one of the fastest
# scripting languages:
# http://mastrodonato.info/index.php/2009/08/comparison-script-languages-for-the-fractal-geometry/
import clr
clr.AddReferenceToFile("bin/mandelbrotbase.dll")
import mandelbrotbase

from System import Random, DateTime, Math
from System.Windows import Visibility
from System.Windows.Controls import UserControl, Canvas
from Microsoft.Scripting.Silverlight import DynamicApplication

class Mandelbrot(UserControl):

    DefaultXS = -2.1
    DefaultYS = -1.3
    DefaultXE = 1.0
    DefaultYE = 1.3

    def __init__(self): 
        print '__init__'
        self.LoadComponent()

        self.StartPoint = None
        self.Randomizer = Random(DateTime.Now.Millisecond)
        self.Generator = mandelbrotbase.MandelbrotGenerator(self, int(self.Content.FractalArea.Width), int(self.Content.FractalArea.Height))
        self.Generator.Completed += self.Generator_Completed
        
        # commands
        self.Content.ResetButton.Click      += lambda sender, e: self.Reset()
        self.Content.ZoomInButton.Click     += lambda sender, e: self.ZoomIn()
        self.Content.ZoomOutButton.Click    += lambda sender, e: self.ZoomOut()
        self.Content.PanLeftButton.Click    += lambda sender, e: self.Pan(-50, 0)
        self.Content.PanRightButton.Click   += lambda sender, e: self.Pan(50, 0)
        self.Content.PanUpButton.Click      += lambda sender, e: self.Pan(0, -50)
        self.Content.PanDownButton.Click    += lambda sender, e: self.Pan(0, 50)
        self.Content.RandomButton.Click     += lambda sender, e: self.Randomize()

        self.Content.FractalArea.MouseLeftButtonDown += self.area_MouseLeftButtonDown
        self.Content.FractalArea.MouseLeftButtonUp   += self.area_MouseLeftButtonUp
        self.Content.FractalArea.MouseMove           += self.area_MouseMove

    def LoadComponent(self):
        print 'LoadComponent'
        xaml = DynamicApplication.LoadComponentFromString(open("mandelbrot.xaml").read())
        xaml.Loaded += self.UserControl_Loaded
        self.Content = xaml

    def Generator_Completed(self, sender, e):
        self.Content.image.ImageSource = e.Image
        self.SetEnabled(True)

    def UserControl_Loaded(self, sender, e):
        print 'UserControl_Loaded'
        self.Reset()

    def ZoomIn(self):
        self.Redraw(50, 50, self.Content.FractalArea.Width - 50, self.Content.FractalArea.Height - 50)

    def ZoomOut(self):
        self.Redraw(-50, -50, self.Content.FractalArea.Width + 50, self.Content.FractalArea.Height + 50)

    def Pan(self, panX, panY):
        self.Redraw(0 + panX, 0 + panY, self.Content.FractalArea.Width + panX, self.Content.FractalArea.Height + panY)

    def Randomize(self):
        self.CurrentXS = Mandelbrot.DefaultXS
        self.CurrentYS = Mandelbrot.DefaultYS
        self.CurrentXE = Mandelbrot.DefaultXE
        self.CurrentYE = Mandelbrot.DefaultYE

        xs = self.Randomizer.Next(0, int(self.Content.FractalArea.Width))
        ys = self.Randomizer.Next(0, int(self.Content.FractalArea.Height))
        w = self.Randomizer.Next(3, 100)
        h = int(w / (self.Content.FractalArea.Width / self.Content.FractalArea.Height))

        self.Redraw(xs, ys, xs + w, ys + h)

    def Reset(self):
        print 'Reset'
        self.CurrentXS = Mandelbrot.DefaultXS
        self.CurrentYS = Mandelbrot.DefaultYS
        self.CurrentXE = Mandelbrot.DefaultXE
        self.CurrentYE = Mandelbrot.DefaultYE
        self.Redraw(0, 0, self.Content.FractalArea.Width, self.Content.FractalArea.Height)

    def area_MouseLeftButtonDown(self, sender, e):
        self.StartPoint = e.GetPosition(self.Content.FractalArea)
        self.Content.selection.Visibility = Visibility.Visible
        self.Content.selection.Width = 0
        self.Content.selection.Height = 0
        Canvas.SetLeft(self.Content.selection, self.StartPoint.X)
        Canvas.SetTop(self.Content.selection, self.StartPoint.Y)
        self.Content.FractalArea.CaptureMouse()

    def area_MouseLeftButtonUp(self, sender, e):
        if self.StartPoint is not None:
            currentPoint = e.GetPosition(self.Content.FractalArea)
            if currentPoint != self.StartPoint:
                if currentPoint.X > self.StartPoint.X:
                    xs = self.StartPoint.X
                else:
                    xs = currentPoint.X
                if currentPoint.Y > self.StartPoint.Y:
                    ys = self.StartPoint.Y
                else:
                    ys = currentPoint.Y
                xe = xs + self.Content.selection.Width
                ye = ys + self.Content.selection.Height

                self.Redraw(xs, ys, xe, ye)

            self.StartPoint = None
            self.Content.selection.Visibility = Visibility.Collapsed
            self.Content.FractalArea.ReleaseMouseCapture()

    def area_MouseMove(self, sender, e):
        if self.StartPoint is not None:
            currentPoint = e.GetPosition(self.Content.FractalArea)

            if currentPoint.X < 0: currentPoint.X = 0
            if currentPoint.Y < 0: currentPoint.Y = 0
            if currentPoint.X > self.Content.FractalArea.Width: currentPoint.X = self.Content.FractalArea.Width
            if currentPoint.Y > self.Content.FractalArea.Height: currentPoint.Y = self.Content.FractalArea.Height

            self.Content.selection.Width = Math.Abs(currentPoint.X - self.StartPoint.X)
            self.Content.selection.Height = self.Content.selection.Width / (self.Content.FractalArea.Width / self.Content.FractalArea.Height)

            if currentPoint.X > self.StartPoint.X:
                canvasLeft = self.StartPoint.X
            else: 
                canvasLeft = currentPoint.X

            if currentPoint.Y > self.StartPoint.Y:
                canvasTop = self.StartPoint.Y
            else:
                canvasTop = currentPoint.Y

            Canvas.SetLeft(self.Content.selection, canvasLeft)
            Canvas.SetTop(self.Content.selection, canvasTop)

    def Redraw(self, xs, ys, xe, ye):
        print 'Redraw'
        self.SetEnabled(False)

        w = self.CurrentXE - self.CurrentXS
        h = self.CurrentYE - self.CurrentYS

        xsp = (xs * 100 / self.Content.FractalArea.Width)
        cxs = (w / 100 * xsp) + self.CurrentXS
        xep = (xe * 100 / self.Content.FractalArea.Width)
        cxe = (w / 100 * xep) + self.CurrentXS
        ysp = (ys * 100 / self.Content.FractalArea.Height)
        cys = (h / 100 * ysp) + self.CurrentYS
        yep = (ye * 100 / self.Content.FractalArea.Height)
        cye = (h / 100 * yep) + self.CurrentYS

        self.CurrentXS = cxs
        self.CurrentXE = cxe
        self.CurrentYS = cys
        self.CurrentYE = cye

        self.Generator.Generate(self.CurrentXS, self.CurrentYS, self.CurrentXE, self.CurrentYE)

    def SetEnabled(self, enabled):
        self.Content.PanDownButton.IsEnabled = enabled
        self.Content.PanLeftButton.IsEnabled = enabled
        self.Content.PanRightButton.IsEnabled = enabled
        self.Content.PanUpButton.IsEnabled = enabled
        self.Content.ZoomInButton.IsEnabled = enabled
        self.Content.ZoomOutButton.IsEnabled = enabled
        self.Content.ResetButton.IsEnabled = enabled
        self.Content.RandomButton.IsEnabled = enabled

from Microsoft.Scripting.Silverlight import DynamicApplication
DynamicApplication.Current.RootVisual = Mandelbrot()