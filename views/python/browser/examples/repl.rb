class Microsoft::Scripting::Silverlight::Repl
  IronRuby = 'silverlightDlrRepl1'
  Minimize = 'silverlightDlrWindowLink'
  Container = 'silverlightDlrWindowContainer'
  
  def hide_all_panels
    window.eval "sdlrw.hideAllPanels(document.getElementById(\"#{Minimize}\"))"
  end
  
  def show_panel(id)
    window.eval "sdlrw.showPanel(\"#{id}\")"
  end
  
  def show_ironruby
    show_panel(IronRuby)
  end
  
  def remove
    document.body.remove_child document.silverlightDlrWindowContainer
  end
end

if document.query_string.contains_key 'console'
  $repl = Microsoft::Scripting::Silverlight::Repl.show('ruby')
  $stdout = $repl.output_buffer
  $stderr = $repl.output_buffer
  if document.query_string['console'] == 'off'
    $repl.hide_all_panels
  else
    $repl.show_ironruby
  end
end
