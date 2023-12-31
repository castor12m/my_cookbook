## reids 실행, brew services in mac

ref : https://stackoverflow.com/questions/6910378/how-can-i-stop-redis-server

```
    $ brew services start|run redis 
    $ brew services stop redis
    $ brew services restart redis
```

## reids 실행, in window

ref <br/>
: https://github.com/microsoftarchive/redis/releases/tag/win-3.2.100 <br/>
: https://itnhappy.tistory.com/328 <br/>
: http://redisgate.kr/redis/introduction/win_start.php <br/>

```powershell
    (Powershell 을 관리자모드로 실행시킨다.)

    1) 실행
    $ cd C:\Program Files\Redis
    $ redis-server.exe redis.windows.conf

    2) 중지
    $ net stop redis
```

## redis 실행, docker 이미지

ref <br/>
: https://hub.docker.com/_/redis <br/>
: https://emflant.tistory.com/235 <br/>
: https://velog.io/@coastby/redis-docker%EB%A1%9C-redis-%EB%9D%84%EC%9A%B0%EA%B8%B0 <br/>

```
    1) redis container 실행
    $ docker run -p 6379:6379 --name (redis 컨테이너 이름) -d redis:latest --requirepass "(비밀번호)"
    
    ex)$ docker run -p 6379:6379 --name docker_redis -d redis:alpine --requirepass "foobared"

    2) redis container - redis-cli 접근
    $ docker exec -i -t (redis 컨테이너 이름) redis-cli -a "비밀번호"

    ex)$ docker exec -i -t docker_redis redis-cli -a "foobared"   

```