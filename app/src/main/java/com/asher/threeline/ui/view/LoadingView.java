package com.asher.threeline.ui.view;

import android.animation.ValueAnimator;
import android.content.Context;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.util.AttributeSet;
import android.util.Log;
import android.view.View;
import android.view.animation.LinearInterpolator;

/**
 * Created by ouyangfan on 17/5/5.
 *
 * loading view
 */

public class LoadingView extends View {

    private ValueAnimator valueAnimator;
    //画笔
    private Paint mPaint;
    //圆形的半径
    private int circleRadius = 20;
    //浮动的边长
    private int halfDistance = 60;
    private float density;
    //颜色的下标
    private int colorIndex = 0;
    //指定的颜色
    private int colors[] = new int[]{Color.parseColor("#EE454A"),Color.parseColor("#2E9AF2"),
            Color.parseColor("#616161")};
    //中心点的x、y，当前点的x
    private int centerX,centerY,currentX;
    //最左边的起始点坐标x
    private int startX;
    public LoadingView(Context context, AttributeSet attrs) {
        super(context, attrs);
        density = getResources().getDisplayMetrics().density;
        Log.i("LoadingView", "density = " + density);
        mPaint = new Paint(Paint.ANTI_ALIAS_FLAG);
    }

    @Override
    protected void onDraw(Canvas canvas) {
        centerX = getWidth()/2;
        centerY = getHeight()/2;
        startX = (int) (centerX - halfDistance * density);
        if(currentX == 0){
            playAnimator();
        }else{
            drawCircle(canvas);
        }
    }

    /**
     * 执行动画
     */
    private void playAnimator(){
        Log.i("LoadingView", "startX = " + startX + " , end = " + (centerX - circleRadius/2));
        valueAnimator = ValueAnimator.ofInt(startX, centerX - circleRadius/2);
        valueAnimator.addUpdateListener(new ValueAnimator.AnimatorUpdateListener() {
            @Override
            public void onAnimationUpdate(ValueAnimator animation) {
                currentX = (int) animation.getAnimatedValue();
                invalidate();
            }
        });
        valueAnimator.setRepeatCount(-1);
        valueAnimator.setDuration(400);
        valueAnimator.setInterpolator(new LinearInterpolator());
        valueAnimator.setRepeatMode(ValueAnimator.REVERSE);
        valueAnimator.start();
    }

    /**
     * 绘制圆形
     * @param canvas
     */
    private void drawCircle(Canvas canvas){
        if(Math.abs(currentX - centerX) <= circleRadius/2){
            colorIndex++;
            mPaint.setColor(colors[colorIndex % 3]);
        }else{
            mPaint.setColor(colors[colorIndex]);
        }
        canvas.drawCircle(centerX, centerY, circleRadius, mPaint);

        mPaint.setColor(colors[(colorIndex + 1) % 3]);
        canvas.drawCircle(currentX, centerY, circleRadius, mPaint);

        mPaint.setColor(colors[(colorIndex + 2) % 3]);
        canvas.drawCircle(2 *centerX - currentX,centerY,circleRadius,mPaint);

        if(colorIndex == 3)colorIndex=0;
    }

    /**
     * 在View销毁时停止动画
     */
    @Override
    protected void onDetachedFromWindow() {
        super.onDetachedFromWindow();
        if (!hasWindowFocus()) {
            endAnimation();
        }
    }

    public void endAnimation() {
        if (null == valueAnimator) {
            return;
        }
        //cancel结束时保留当前动画值
        valueAnimator.cancel();
        //end结束时会计算最终值
        valueAnimator.end();
    }

}
