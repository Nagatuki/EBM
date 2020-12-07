# データの取得と描画

## 計画
- まずはPythonで
  - pySerialでRS232Cからデータを取得する
  - matplotlibを使ってリアルタイムでグラフ表示を行う

- C#で
  - Pythonで重かった場合
  - スクリプト言語によるデータ取得＆描画よりは速いだろうという話
    - でもグラフィック周りの実装は別言語だから関係なさそう
  - Visual Studioにお世話になるのやだなぁ
  - 言語が把握しきれなかったらパスする

- C++で
  - C#に心折れた場合
  - C#でも遅かった場合
  - グラフィック処理をどうしようか
    - 高速化図るならOpenGL
    - 学習コスト考えるなら他のグラフィックライブラリ
  - 言語に慣れているのがつよみ
  - windows.h
  - Boostにもシリアルポート用ライブラリが入っているらしい

## Pythonで

### 参考サイト

- pySerial
  - https://qiita.com/asakuraTsukazaki/items/84cd96af907d71028bac
  - https://qiita.com/nonbiri15/items/2211547da4dc9abcc321
  - https://serip39.hatenablog.com/entry/2020/07/03/070000
  - https://armadillo.atmark-techno.com/blog/615/3617
  - https://dekirukigasuru.com/blog/2017/03/18/python-pyserial/
  - 検索
    - https://www.google.com/search?q=python+%E3%82%B7%E3%83%AA%E3%82%A2%E3%83%AB%E9%80%9A%E4%BF%A1+windows&oq=pythn+%E3%81%97%E3%82%8A%E3%81%82&aqs=chrome.5.69i57j0i13l7.10194j0j7&sourceid=chrome&ie=UTF-8
  - 

- matplotlib
  - https://qiita.com/bridget462/items/710cd42b3ee1f8780260

## C#で

### 参考になるかもしれないサイト

https://www.google.com/search?q=.net+framework+rs232c&oq=.net+framework+rs&aqs=chrome.1.69i57j0i30l4j0i8i30l3.8925j0j7&sourceid=chrome&ie=UTF-8
https://blog.tes.co.jp/entry/2018/05/15/092009
https://www.google.com/search?sxsrf=ALeKk02lWdUSHsE7uy8f-moIXBLAc1l8Kg%3A1606808216456&ei=mPLFX-qsG9GRr7wP8JCi0Aw&q=.net+framework+%E3%82%B0%E3%83%A9%E3%83%95%E3%80%80%E3%83%AA%E3%82%A2%E3%83%AB%E3%82%BF%E3%82%A4%E3%83%A0%E3%80%80C%2B%2B&oq=.net+framework+%E3%82%B0%E3%83%A9%E3%83%95%E3%80%80%E3%83%AA%E3%82%A2%E3%83%AB%E3%82%BF%E3%82%A4%E3%83%A0%E3%80%80C%2B%2B&gs_lcp=CgZwc3ktYWIQAzoECCMQJzoFCAAQzQJQj8kCWN_RAmCJ1QJoAHAAeACAAYgBiAGNBJIBAzMuMpgBAKABAaoBB2d3cy13aXrAAQE&sclient=psy-ab&ved=0ahUKEwjq2NqHo6ztAhXRyIsBHXCICMoQ4dUDCA0&uact=5
https://codezine.jp/article/detail/6812
https://social.msdn.microsoft.com/Forums/ja-JP/7f3ec2c4-10a0-47ee-aa77-9803f4ccbd97/12509125401248812363124251252212450125231247912452125122145438?forum=vsgeneralja
https://www.atmarkit.co.jp/ait/articles/1007/22/news111.html
https://blog.goo.ne.jp/yamadokoro/e/bf81479f774632670ef892a8a6196937
http://www.kanazawa-net.ne.jp/~pmansato/net/net_compo_mschart.htm
https://www.google.com/search?q=Visual+basic+%E3%82%B0%E3%83%A9%E3%83%95&oq=Visual+basic+%E3%82%B0%E3%83%A9%E3%83%95&aqs=chrome..69i57j0l4.7398j0j7&sourceid=chrome&ie=UTF-8



## C++で

- OpenGL
  - http://titech-ssr.blog.jp/archives/1048225188.html
  - https://tokoik.github.io/GLFWdraft.pdf
  - http://marina.sys.wakayama-u.ac.jp/~tokoi/?date=20120906
  - https://nn-hokuson.hatenablog.com/entry/2014/01/10/201729
  - http://www.opengl-tutorial.org/jp/beginners-tutorials/tutorial-1-opening-a-window/
  - https://codelabo.com/posts/20200228124232
  - http://www.sanko-shoko.net/note.php?id=3xnt

  - https://qiita.com/kcha4tsubuyaki/items/7d6388129714ca6c48ea
  - https://matcha-choco010.net/2020/03/29/opengl-glfw-window/

- matplotlibを作る
  - https://www.google.com/search?q=c%2B%2B+%E3%82%B0%E3%83%A9%E3%83%95+%E6%8F%8F%E7%94%BB&oq=c%2B%2B+%E3%82%B0%E3%83%A9%E3%83%95+%E6%8F%8F%E7%94%BB%E3%80%80&aqs=chrome..69i57j0j0i8i30l2j0i5i30l2.6030j0j7&sourceid=chrome&ie=UTF-8
  - https://trap.jp/post/1080/
  - https://hirlab.net/nblog/category/programming/art_826/
  - https://github.com/lava/matplotlib-cpp

- win32api
  - https://www.saluteweb.net/~oss_winapi232.html
  - https://www.google.com/search?q=windows+api+%E3%82%B7%E3%83%AA%E3%82%A2%E3%83%AB%E9%80%9A%E4%BF%A1&oq=windows+api+%E3%81%97%E3%82%8A%E3%81%82&aqs=chrome.1.69i57j0i4j0i4i30.9521j0j7&sourceid=chrome&ie=UTF-8


