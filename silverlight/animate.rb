#include Microsoft::Scripting::Silverlight
#repl = Repl.show
#$stdout = repl.OutputBuffer
#$stderr = repl.OutputBuffer

codebox = document.send('code-snippet').children.first
codebox.mouseover do |s, e|
  s.set_style_attribute 'width', '350px'
  s.set_style_attribute 'backgroundColor', '#484848'
end
codebox.mouseout do |s, e|
  s.set_style_attribute 'width', '200px'
  s.set_style_attribute 'backgroundColor', 'transparent'
end
