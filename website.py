# how can use python write website
> class _Engine(object):
>     def __init__(self,connect):
>         self._connect=connect
>     def connect(self):
>         return self._connect()
> engine=None
> class _DbCtx(threading.local):
>     def __init__(self):
>         self.connection=None
>         self.transactions=0
>     def is_init(self):
>         return not self.connection is None
>     def init(self):
>         self.connection=_LasyConnection()
>         self.transactions=0
>     def cleanup(self):
>         self.connection.cleanup()
>         self.transactions=0
>     def cursor(self):
>         return self.conection.cursor()
> _db_ctx=_DbCtx()
> class _ConnectionCtx(object):
>     def __enter__(self):
>         global _db_ctx
>         self.should_cleanup=False
>         if not _db_ctx.is_init():
>             _db_ctx.init()
>             self.should_cleanup=True
>         return self
>     def __exit__(self,exctype,excvalue,traceback):
>         global _db_ctx
>         if self.should_cleanup:
>             _db_ctx.cleanup()
>     def connection():
>         return _ConnectionCtx()
> with connection():
>     do_some_db_operation()
> @with_connection
> def select(sql,*arqs):
>     pass
> @with_connection
> def update(sql,*arqs):
>     pass
> with db.transaction():
>     db.select('...')
>     db.update('...')
>     db.update('...')
> class _TransactionCtx(object):
>     def __enter__(self):
>         global _db_ctx
>         self.should_close_conn==False
>         if not _db_ctx.is_init():
>             _db_ctx.init()
>             self.should_close_conn=True
>         _db_ctx.transactions=_db_ctx.transactions + 1
>         return self
>     def _exit_(self,exctype,excvalue,traceback):
>         global _db_ctx
>         _db_ctx.transactions = _db_ctx.transactions - 1
>         try:
>             if _db_ctx.transactions==0:
>                 if exctype is None:
>                     self.commit()
>                 else:
>                     self.rollback()
>         finally:
>             if self.should_close_conn:
>                 _db_ctx.cleanup()
>     def commit(self):
>         global _db_ctx
>         try:
>             _db_ctx.connection.commit()
>         except:
>             _db_ctx.connection.rollback()
>             raise
>     def rollback(self):
>         global _db_ctx
>         _db_ctx.connection.rollback()
