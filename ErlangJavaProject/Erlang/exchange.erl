-module(exchange).
-export([start/0]).
-export([init/0]).
-import(calling,[loop/0]).

start() ->
  {ok,T_List} = file:consult("calls.txt"),
  io:fwrite("** Calls to be made **~n~n"),
  lists:map(fun(X)->

    io:fwrite("~w: ",[element(1,X)]),
    io:fwrite("~w~n",[element(2,X)])
            end, T_List),
  io:fwrite("~n"),

  Pid=spawn(exchange,init,[]),
  register(master,Pid),
  master!{T_List},
  timer:sleep(1).

init()->
  receive
    {T_List}->
      lists:map(fun(X)->
        Hd=element(1,X),
        Tl=element(2,X),
        Pid=spawn(calling,loop,[]),
        register(Hd,Pid),
        Hd!{Hd,Tl}
                end, T_List),
      init();
    {intro,TimeInMicro,X,Hd}->
      timer:sleep(random:uniform(100)),
      io:fwrite("~w received intro message from ~w [~w]~n",[X,Hd,TimeInMicro]),

      init();
    {reply,TimeInMicro,X,Hd}->
      io:fwrite("~w received reply message from ~w [~w]~n",[Hd,X,TimeInMicro]),

      init()

  after
    1000->
      {_, List} = file:consult("calls.txt"),
      lists:map(fun(X) -> {Y,_} = X, Y ! stop,
        timer:sleep(round(timer:seconds(random:uniform())))
                end, List),
      timer:sleep(100),
      io:fwrite("Master has received no replies for 1.5 seconds, ending...~n"),
      exit(kill)

  end.