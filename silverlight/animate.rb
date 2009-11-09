#include Microsoft::Scripting::Silverlight
#repl = Repl.show
#$stdout = repl.OutputBuffer
#$stderr = repl.OutputBuffer

codebox = document.send('code-snippet').children.first
codebox.mouseover do |s, e|
  s.set_style_attribute 'width', '350px'
end
codebox.mouseout do |s, e|
  s.set_style_attribute 'width', '200px'
end
