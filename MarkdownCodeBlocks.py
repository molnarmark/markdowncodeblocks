import sublime
import sublime_plugin

class MarkdownAddCodeBlockCommand(sublime_plugin.TextCommand):
  def run(self, edit, key = '', val = '', save = True):
    self._input = self.view.window().show_input_panel('Language Name', '', self.on_done, self.on_change, self.on_close)

    self.on_change(path)

  def on_done(self, language):
    self.view.run_command('markdown_insert_code_block', {
      'args': {
        'language': language
      }
    })

  def on_close(self):
    pass

  def on_change(self):
    pass

class MarkdownInsertCodeBlockCommand(sublime_plugin.TextCommand):
  def run(self, edit, args):
    lang_name = args['language']
    if not lang_name:
      lang_name = ''

    self.view.run_command('insert_snippet', {
      'contents': '```' + lang_name + '\n$0\n```'
    })