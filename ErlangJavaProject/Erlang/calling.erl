-module(calling).
-export([loop/0]).

%% API
loop()->
  receive
    {Hd,Tl}->
      lists:foreach(fun(X)->
        Time=erlang:now(),
        TimeInMicro=element(3,Time),
        X!{intro,TimeInMicro,X,Hd}
                    end,Tl),
      loop();
    {intro,TimeInMicro,X,Hd}->
      timer:sleep(random:uniform(100)),
      master!{intro,TimeInMicro,X,Hd},
      Hd!{reply,TimeInMicro,X,Hd},
      loop();
    {reply,TimeInMicro,X,Hd}->
      timer:sleep(random:uniform(100)),
      master!{reply,TimeInMicro,X,Hd},
      loop();
    stop ->
      {_,PName} = erlang:process_info(self(), registered_name),
      io:format("~nProcess ~p has received no calls for 1 second, ending...~n~n",[PName]),
      exit(kill)
  end.