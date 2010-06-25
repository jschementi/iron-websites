include Microsoft::Scripting::Silverlight

if document.query_string.contains_key 'console'
  repl = Repl.show
  $stdout = repl.OutputBuffer
  $stderr = repl.OutputBuffer
end

codebox = document.send('code-snippet').children.first
codebox.mouseover do |s, e|
  s.set_style_attribute 'width', '350px'
end
codebox.mouseout do |s, e|
  s.set_style_attribute 'width', '200px'
end
