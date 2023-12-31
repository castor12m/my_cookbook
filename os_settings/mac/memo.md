
### 1. mac


### 1.2 zsh 실행시 bash_profile 실행

```
    (~/.zshrc)

    if [ -f ~/.bash_profile ]; then
        . ~/.bash_profile   # 물론 해당 파일이 존재해야함
    fi
```

```
    (~/.bash_profile)
   
```

### 1.3 zsh 테마 설정을 위한 oh my zsh 설치

https://bobr2.tistory.com/entry/%EB%A7%A5%EB%B6%81-Oh-My-Zsh-%EC%84%A4%EC%B9%98-%EB%B0%A9%EB%B2%95

https://ohmyz.sh/

!! 주의 설치하게 되면 기존에 ~/.zshrc 가 새로운 설정으로 덮어짐

```console
   $ sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

글꼴 설치 (안하면 맥기본 터미널시 폰트 깨짐)

### 1.3.1 네이버 배포 D2Coding 글꼴 설치법

1. https://github.com/naver/d2codingfont/releases 에서 최신 버전 압축 파일 다운

2. 압축 해제

3. D2CoddingAll 폴더의 D2Codding-Verx.x-xxxxxx-all.ttc 파일 열기 클릭

4. 모음 설치


### 2. python 링크 

homebrew로 python3 설치시, python 명령만으로 python3 접근하려고 할 때

https://velog.io/@kyliecamila_/homebrew-python-version%EB%B3%80%EA%B2%BD

```
    which python3로 파이썬 경로를 알아내고
    -->/opt/homebrew/bin/python3
    이 경로는 내가 ~/.zshrc에 export PATH="/opt/homebrew/bin:$PATH:"를 적어서 경로가 이런것이다.

    ls -l <찾은 경로 python 전까지>/python*
    ls -l /opt/homebrew/bin/python*
    에서 원하는 버전이 있는지 확인후

    ln -s -f /opt/homebrew/bin/python<원하는버전> /opt/homebrew/bin/python
    e.g) ln -s -f /opt/homebrew/bin/python3.10 /opt/homebrew/bin/python

    터미널 껐다가 켜고 python --version

    바뀌지 않았으면

    brew unlink python@<끊고싶은버전>
    e.g) brew unlink python@3.8
    brew link --force python@<연결하고싶은버전>
    e.g) brew link --force python@3.10

    여기까지만 해도 되지만 이후에 which python3를 했을때 경로가 약간 달라질 것이기에 다시 복구하기 위해

    vi ~/.zshrc 또는 code ~/.zshrc
    후자로 하면 vscode에서 열린다
    거기서 /opt/homebrew/bin/python3외에
    /opt/homebrew/bin/python<원하는버전>인것이 있을것이다. 그거 삭제.

    vi ~/.zshrc로 열었다면 새로 삽입하기위해 i를 누르고 원하는 곳에 변화를 준후 esc를 누른후 :wq(저장후 나가기)

    변경사항을 반영하기 위해서
    source ~/.zshrc
    저장하고 다시 which python3해보면 원래 경로가 나올 것이다.
```


