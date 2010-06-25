using System;
using System.Net;
using System.Linq;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Documents;
using System.Windows.Ink;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Animation;
using System.Windows.Shapes;
using System.Collections.Generic;
using System.Windows.Media.Imaging;
using System.ComponentModel;
using System.Threading;

namespace mandelbrotbase
{
    public class MandelbrotGenerator
    {
        /// <summary>
        /// Occurs when [completed].
        /// </summary>
        public event EventHandler<CompletedEventArgs> Completed;
        /// <summary>
        /// Gets or sets the palette.
        /// </summary>
        /// <value>The palette.</value>
        private Color[] Palette { get; set; }
        /// <summary>
        /// Gets or sets the width.
        /// </summary>
        /// <value>The width.</value>
        public int Width { get; set; }
        /// <summary>
        /// Gets or sets the height.
        /// </summary>
        /// <value>The height.</value>
        public int Height { get; set; }
        /// <summary>
        /// Gets or sets the UI element.
        /// </summary>
        /// <value>The UI element.</value>
        public UIElement UIElement { get; set; }

        /// <summary>
        /// Initializes a new instance of the <see cref="MandelbrotGenerator"/> class.
        /// </summary>
        public MandelbrotGenerator(UIElement uiElement, int width, int height)
        {
            this.UIElement = uiElement;
            this.Width = width;
            this.Height = height;
            this.Palette = GeneratePalette();
        }

        /// <summary>
        /// Draws the specified sx.
        /// </summary>
        /// <param name="sx">The sx.</param>
        /// <param name="sy">The sy.</param>
        /// <param name="fx">The fx.</param>
        /// <param name="fy">The fy.</param>
        /// <returns></returns>
        private void Draw(object state)
        {
            GenerationState size = state as GenerationState;

            if (size == null)
                throw new InvalidOperationException();

            int[] bmap = new int[this.Width * this.Height];

            // Creates the Bitmap we draw to
            // From here on out is just converted from the c++ version.
            double x, y, x1, y1, xx, xmin, xmax, ymin, ymax = 0.0;

            int looper, s, z = 0;
            double intigralX, intigralY = 0.0;
            xmin = size.SX; // Start x value, normally -2.1
            ymin = size.SY; // Start y value, normally -1.3
            xmax = size.FX; // Finish x value, normally 1
            ymax = size.FY; // Finish y value, normally 1.3
            intigralX = (xmax - xmin) / this.Width; // Make it fill the whole window
            intigralY = (ymax - ymin) / this.Height;
            x = xmin;

            for (s = 0; s < this.Width; s++)
            {
                y = ymin;
                for (z = 0; z < this.Height; z++)
                {
                    x1 = 0;
                    y1 = 0;
                    looper = 0;

                    while (looper < 100 && ((x1 * x1) + (y1 * y1)) < 4)
                    {
                        looper++;
                        xx = (x1 * x1) - (y1 * y1) + x;
                        y1 = 2 * x1 * y1 + y;
                        x1 = xx;
                    }

                    // Get the percent of where the looper stopped
                    double perc = looper / (100.0);
                    // Get that part of a 255 scale
                    int val = ((int)(perc * (this.Palette.Length - 1)));
                    // Use that number to set the color

                    Color px = this.Palette[val];
                    bmap[z * this.Width + s] = px.A << 24 | px.R << 16 | px.G << 8 | px.B;

                    y += intigralY;
                }

                x += intigralX;
            }

            this.UIElement.Dispatcher.BeginInvoke(
                new Action<int[]>(
                    data =>
                    {
                        WriteableBitmap output = new WriteableBitmap(this.Width, this.Height);

                        try
                        {                            
                            for (int i = 0; i < data.Length; i++) 
                                output.Pixels[i] = data[i];

                            this.OnCompleted(new CompletedEventArgs(output));
                        }
                        finally
                        {
                            output.Invalidate();
                        }

                    }), bmap);
        }

        /// <summary>
        /// Generates the palette.
        /// </summary>
        /// <returns></returns>
        private Color[] GeneratePalette()
        {
            List<Color> colors = new List<Color>();

            for (int c = 0; c < 256; c++)
                colors.Add(Color.FromArgb(0xff, (byte)c, 0, 0));
            for (int c = 0; c < 256; c++)
                colors.Add(Color.FromArgb(0xff, 0xff, 0, (byte)c));
            for (int c = 255; c >= 0; c--)
                colors.Add(Color.FromArgb(0xff, (byte)c, 0, 0xff));
            for (int c = 0; c < 256; c++)
                colors.Add(Color.FromArgb(0xff, 0, (byte)c, 0xff));
            for (int c = 255; c >= 0; c--)
                colors.Add(Color.FromArgb(0xff, 0, 0xff, (byte)c));
            for (int c = 0; c < 256; c++)
                colors.Add(Color.FromArgb(0xff, 0, (byte)c, 0xff));
            for (int c = 255; c >= 0; c--)
                colors.Add(Color.FromArgb(0xff, (byte)c, 0, 0xff));
            for (int c = 0; c < 256; c++)
                colors.Add(Color.FromArgb(0xff, 0xff, 0, (byte)c));
            for (int c = 0; c < 256; c++)
                colors.Add(Color.FromArgb(0xff, (byte)c, 0, 0));

            var half =
                colors.Concat(
                    colors.Reverse<Color>());

            return half.Concat(half).ToArray();
        }

        /// <summary>
        /// Raises the <see cref="E:Completed"/> event.
        /// </summary>
        /// <param name="e">The <see cref="Elite.Silverlight3.Fractals.Silverlight.CompletedEventArgs"/> instance containing the event data.</param>
        private void OnCompleted(CompletedEventArgs e)
        {
            EventHandler<CompletedEventArgs> handler = Completed;

            if (handler != null)
                handler(this, e);
        }

        /// <summary>
        /// Generates the specified sx.
        /// </summary>
        /// <param name="sx">The sx.</param>
        /// <param name="sy">The sy.</param>
        /// <param name="fx">The fx.</param>
        /// <param name="fy">The fy.</param>
        public void Generate(double sx, double sy, double fx, double fy)
        {
            ThreadPool.QueueUserWorkItem(
                new WaitCallback(Draw), new GenerationState { SX = sx, SY = sy, FX = fx, FY = fy });
        }

        /// <summary>
        /// 
        /// </summary>
        private class GenerationState
        {
            public double SX { get; set; }
            public double SY { get; set; }
            public double FX { get; set; }
            public double FY { get; set; }
        }
    }

    public class CompletedEventArgs : EventArgs
    {
        /// <summary>
        /// Gets or sets the image.
        /// </summary>
        /// <value>The image.</value>
        public ImageSource Image { get; set; }

        /// <summary>
        /// Initializes a new instance of the <see cref="CompletedEventArgs"/> class.
        /// </summary>
        /// <param name="image">The image.</param>
        public CompletedEventArgs(ImageSource image)
        {
            this.Image = image;
        }
    }
}
