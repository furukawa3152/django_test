/* 最初の画面ここから */
document.addEventListener('DOMContentLoaded', function() {
  const firstScreen = document.querySelector('.first-screen');

  firstScreen.addEventListener('click', function() {
      firstScreen.classList.add('turn-page');  // 新しいアニメーションクラスを追加

      // アニメーション終了後に要素を非表示にする
      firstScreen.addEventListener('animationend', () => {
          firstScreen.style.display = 'none';
      });
  });
});
/* 最初の画面ここまで */