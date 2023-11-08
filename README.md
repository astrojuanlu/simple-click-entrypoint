# simple-click-entrypoint

https://github.com/pallets/click/issues/1054, https://github.com/pallets/click/issues/2249

```
$ python -q
>>> from simple_click_entrypoint.ep import main
>>> main(standalone_mode=False)
>>> 1 + 1
2
>>> main()
$ # oops
```

```
$ ipython --no-banner

In [1]: from simple_click_entrypoint.ep import main

In [2]: main(standalone_mode=False)
---------------------------------------------------------------------------
NoSuchOption                              Traceback (most recent call last)
Cell In[2], line 1
----> 1 main(standalone_mode=False)

File ~/.micromamba/envs/kedro38-dev/lib/python3.8/site-packages/click/core.py:1130, in BaseCommand.__call__(self, *args, **kwargs)
   1128 def __call__(self, *args: t.Any, **kwargs: t.Any) -> t.Any:
   1129     """Alias for :meth:`main`."""
-> 1130     return self.main(*args, **kwargs)

File ~/.micromamba/envs/kedro38-dev/lib/python3.8/site-packages/click/core.py:1054, in BaseCommand.main(self, args, prog_name, complete_var, standalone_mode, windows_expand_args, **extra)
   1052 try:
   1053     try:
-> 1054         with self.make_context(prog_name, args, **extra) as ctx:
   1055             rv = self.invoke(ctx)
   1056             if not standalone_mode:

File ~/.micromamba/envs/kedro38-dev/lib/python3.8/site-packages/click/core.py:920, in BaseCommand.make_context(self, info_name, args, parent, **extra)
    915 ctx = self.context_class(
    916     self, info_name=info_name, parent=parent, **extra  # type: ignore
    917 )
    919 with ctx.scope(cleanup=False):
--> 920     self.parse_args(ctx, args)
    921 return ctx

File ~/.micromamba/envs/kedro38-dev/lib/python3.8/site-packages/click/core.py:1375, in Command.parse_args(self, ctx, args)
   1372     ctx.exit()
   1374 parser = self.make_parser(ctx)
-> 1375 opts, args, param_order = parser.parse_args(args=args)
   1377 for param in iter_params_for_processing(param_order, self.get_params(ctx)):
   1378     value, args = param.handle_parse_result(ctx, opts, args)

File ~/.micromamba/envs/kedro38-dev/lib/python3.8/site-packages/click/parser.py:337, in OptionParser.parse_args(self, args)
    335 state = ParsingState(args)
    336 try:
--> 337     self._process_args_for_options(state)
    338     self._process_args_for_args(state)
    339 except UsageError:

File ~/.micromamba/envs/kedro38-dev/lib/python3.8/site-packages/click/parser.py:364, in OptionParser._process_args_for_options(self, state)
    362     return
    363 elif arg[:1] in self._opt_prefixes and arglen > 1:
--> 364     self._process_opts(arg, state)
    365 elif self.allow_interspersed_args:
    366     state.largs.append(arg)

File ~/.micromamba/envs/kedro38-dev/lib/python3.8/site-packages/click/parser.py:514, in OptionParser._process_opts(self, arg, state)
    510 # At this point we will match the (assumed) long option through
    511 # the long option matching code.  Note that this allows options
    512 # like "-foo" to be matched as long options.
    513 try:
--> 514     self._match_long_opt(norm_long_opt, explicit_value, state)
    515 except NoSuchOption:
    516     # At this point the long option matching failed, and we need
    517     # to try with short options.  However there is a special rule
   (...)
    520     # short option code and will instead raise the no option
    521     # error.
    522     if arg[:2] not in self._opt_prefixes:

File ~/.micromamba/envs/kedro38-dev/lib/python3.8/site-packages/click/parser.py:398, in OptionParser._match_long_opt(self, opt, explicit_value, state)
    395     from difflib import get_close_matches
    397     possibilities = get_close_matches(opt, self._long_opt)
--> 398     raise NoSuchOption(opt, possibilities=possibilities, ctx=self.ctx)
    400 option = self._long_opt[opt]
    401 if option.takes_value:
    402     # At this point it's safe to modify rargs by injecting the
    403     # explicit value, because no exception is raised in this
    404     # branch.  This means that the inserted value will be fully
    405     # consumed.

NoSuchOption: No such option: --no-banner

In [3]: main()
Usage: ipython [OPTIONS]
Try 'ipython --help' for help.

Error: No such option: --no-banner
---------------------------------------------------------------------------
NoSuchOption                              Traceback (most recent call last)
File ~/.micromamba/envs/kedro38-dev/lib/python3.8/site-packages/click/core.py:1054, in BaseCommand.main(self, args, prog_name, complete_var, standalone_mode, windows_expand_args, **extra)
   1053 try:
-> 1054     with self.make_context(prog_name, args, **extra) as ctx:
   1055         rv = self.invoke(ctx)

File ~/.micromamba/envs/kedro38-dev/lib/python3.8/site-packages/click/core.py:920, in BaseCommand.make_context(self, info_name, args, parent, **extra)
    919 with ctx.scope(cleanup=False):
--> 920     self.parse_args(ctx, args)
    921 return ctx

File ~/.micromamba/envs/kedro38-dev/lib/python3.8/site-packages/click/core.py:1375, in Command.parse_args(self, ctx, args)
   1374 parser = self.make_parser(ctx)
-> 1375 opts, args, param_order = parser.parse_args(args=args)
   1377 for param in iter_params_for_processing(param_order, self.get_params(ctx)):

File ~/.micromamba/envs/kedro38-dev/lib/python3.8/site-packages/click/parser.py:337, in OptionParser.parse_args(self, args)
    336 try:
--> 337     self._process_args_for_options(state)
    338     self._process_args_for_args(state)

File ~/.micromamba/envs/kedro38-dev/lib/python3.8/site-packages/click/parser.py:364, in OptionParser._process_args_for_options(self, state)
    363 elif arg[:1] in self._opt_prefixes and arglen > 1:
--> 364     self._process_opts(arg, state)
    365 elif self.allow_interspersed_args:

File ~/.micromamba/envs/kedro38-dev/lib/python3.8/site-packages/click/parser.py:514, in OptionParser._process_opts(self, arg, state)
    513 try:
--> 514     self._match_long_opt(norm_long_opt, explicit_value, state)
    515 except NoSuchOption:
    516     # At this point the long option matching failed, and we need
    517     # to try with short options.  However there is a special rule
   (...)
    520     # short option code and will instead raise the no option
    521     # error.

File ~/.micromamba/envs/kedro38-dev/lib/python3.8/site-packages/click/parser.py:398, in OptionParser._match_long_opt(self, opt, explicit_value, state)
    397     possibilities = get_close_matches(opt, self._long_opt)
--> 398     raise NoSuchOption(opt, possibilities=possibilities, ctx=self.ctx)
    400 option = self._long_opt[opt]

NoSuchOption: No such option: --no-banner

During handling of the above exception, another exception occurred:

SystemExit                                Traceback (most recent call last)
    [... skipping hidden 1 frame]

Cell In[3], line 1
----> 1 main()

File ~/.micromamba/envs/kedro38-dev/lib/python3.8/site-packages/click/core.py:1130, in BaseCommand.__call__(self, *args, **kwargs)
   1129 """Alias for :meth:`main`."""
-> 1130 return self.main(*args, **kwargs)

File ~/.micromamba/envs/kedro38-dev/lib/python3.8/site-packages/click/core.py:1073, in BaseCommand.main(self, args, prog_name, complete_var, standalone_mode, windows_expand_args, **extra)
   1072     e.show()
-> 1073     sys.exit(e.exit_code)
   1074 except OSError as e:

SystemExit: 2

During handling of the above exception, another exception occurred:

AttributeError                            Traceback (most recent call last)
    [... skipping hidden 1 frame]

File ~/.micromamba/envs/kedro38-dev/lib/python3.8/site-packages/IPython/core/interactiveshell.py:2047, in InteractiveShell.showtraceback(self, exc_tuple, filename, tb_offset, exception_only, running_compiled_code)
   2044 if exception_only:
   2045     stb = ['An exception has occurred, use %tb to see '
   2046            'the full traceback.\n']
-> 2047     stb.extend(self.InteractiveTB.get_exception_only(etype,
   2048                                                      value))
   2049 else:
   2050     try:
   2051         # Exception classes can customise their traceback - we
   2052         # use this in IPython.parallel for exceptions occurring
   2053         # in the engines. This should return a list of strings.

File ~/.micromamba/envs/kedro38-dev/lib/python3.8/site-packages/IPython/core/ultratb.py:636, in ListTB.get_exception_only(self, etype, value)
    628 def get_exception_only(self, etype, value):
    629     """Only print the exception type and message, without a traceback.
    630
    631     Parameters
   (...)
    634     value : exception value
    635     """
--> 636     return ListTB.structured_traceback(self, etype, value)

File ~/.micromamba/envs/kedro38-dev/lib/python3.8/site-packages/IPython/core/ultratb.py:503, in ListTB.structured_traceback(self, etype, evalue, etb, tb_offset, context)
    500     chained_exc_ids.add(id(exception[1]))
    501     chained_exceptions_tb_offset = 0
    502     out_list = (
--> 503         self.structured_traceback(
    504             etype, evalue, (etb, chained_exc_ids),
    505             chained_exceptions_tb_offset, context)
    506         + chained_exception_message
    507         + out_list)
    509 return out_list

File ~/.micromamba/envs/kedro38-dev/lib/python3.8/site-packages/IPython/core/ultratb.py:1288, in AutoFormattedTB.structured_traceback(self, etype, value, tb, tb_offset, number_of_lines_of_context)
   1286 else:
   1287     self.tb = tb
-> 1288 return FormattedTB.structured_traceback(
   1289     self, etype, value, tb, tb_offset, number_of_lines_of_context)

File ~/.micromamba/envs/kedro38-dev/lib/python3.8/site-packages/IPython/core/ultratb.py:1177, in FormattedTB.structured_traceback(self, etype, value, tb, tb_offset, number_of_lines_of_context)
   1174 mode = self.mode
   1175 if mode in self.verbose_modes:
   1176     # Verbose modes need a full traceback
-> 1177     return VerboseTB.structured_traceback(
   1178         self, etype, value, tb, tb_offset, number_of_lines_of_context
   1179     )
   1180 elif mode == 'Minimal':
   1181     return ListTB.get_exception_only(self, etype, value)

File ~/.micromamba/envs/kedro38-dev/lib/python3.8/site-packages/IPython/core/ultratb.py:1030, in VerboseTB.structured_traceback(self, etype, evalue, etb, tb_offset, number_of_lines_of_context)
   1021 def structured_traceback(
   1022     self,
   1023     etype: type,
   (...)
   1027     number_of_lines_of_context: int = 5,
   1028 ):
   1029     """Return a nice text document describing the traceback."""
-> 1030     formatted_exception = self.format_exception_as_a_whole(etype, evalue, etb, number_of_lines_of_context,
   1031                                                            tb_offset)
   1033     colors = self.Colors  # just a shorthand + quicker name lookup
   1034     colorsnormal = colors.Normal  # used a lot

File ~/.micromamba/envs/kedro38-dev/lib/python3.8/site-packages/IPython/core/ultratb.py:935, in VerboseTB.format_exception_as_a_whole(self, etype, evalue, etb, number_of_lines_of_context, tb_offset)
    932 assert isinstance(tb_offset, int)
    933 head = self.prepare_header(etype, self.long_header)
    934 records = (
--> 935     self.get_records(etb, number_of_lines_of_context, tb_offset) if etb else []
    936 )
    938 frames = []
    939 skipped = 0

File ~/.micromamba/envs/kedro38-dev/lib/python3.8/site-packages/IPython/core/ultratb.py:1002, in VerboseTB.get_records(self, etb, number_of_lines_of_context, tb_offset)
   1000 tbs = []
   1001 while cf is not None:
-> 1002     source_file = inspect.getsourcefile(etb.tb_frame)
   1003     lines, first = inspect.getsourcelines(etb.tb_frame)
   1004     max_len = max(max_len, first + len(lines))

AttributeError: 'tuple' object has no attribute 'tb_frame'

In [5]: 1 + 1
Out[5]: 2

In [6]:
Do you really want to exit ([y]/n)? ^D
$ 
```
