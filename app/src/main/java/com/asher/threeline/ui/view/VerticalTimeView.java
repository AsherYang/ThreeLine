package com.asher.threeline.ui.view;

import android.content.Context;
import android.graphics.Canvas;
import android.graphics.Paint;
import android.graphics.Path;
import android.graphics.Rect;
import android.text.TextUtils;
import android.util.AttributeSet;
import android.widget.TextView;

import com.asher.threeline.R;

import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Locale;

/**
 * Created by ouyangfan on 17/6/26.
 * <p>
 * 自定义垂直时间类
 * 适用于sentence 页面时间 2017/05/11 竖直显示
 */
public class VerticalTimeView extends TextView {

    private String mTime;

    private Rect mTextBounds = new Rect();
    private Rect mTextBoundInners = new Rect();
    private Path mPath = new Path();
    private static final int PADDING = 5;

    public VerticalTimeView(Context context) {
        super(context);
        init();
    }

    public VerticalTimeView(Context context, AttributeSet attrs) {
        super(context, attrs);
        init();
    }

    public VerticalTimeView(Context context, AttributeSet attrs, int defStyleAttr) {
        super(context, attrs, defStyleAttr);
        init();
    }

    private void init() {
        getPaint().setColor(getCurrentTextColor());
    }

    /**
     * 设置显示时间
     *
     * @param date 时间 2017/05/11
     */
    public void setTime(String date) {
        mTime = date;
        requestLayout();
    }

    /**
     * 设置显示时间
     *
     * @param date {@link Date}
     */
    public void setTime(Date date) {
        SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy/MM/dd", Locale.CHINA);
        mTime = dateFormat.format(date);
        requestLayout();
    }

    @Override
    protected void onMeasure(int widthMeasureSpec, int heightMeasureSpec) {
        if (TextUtils.isEmpty(mTime)) {
            super.onMeasure(widthMeasureSpec, heightMeasureSpec);
            return;
        }
        getPaint().getTextBounds(mTime, 0, mTime.length(), mTextBounds);
        setMeasuredDimension(measuredWidth(widthMeasureSpec), measuredHeight(heightMeasureSpec));
    }

    private int measuredWidth(int measureSpec) {
        int result = 0;
        int specMode = MeasureSpec.getMode(measureSpec);
        int specSize = MeasureSpec.getSize(measureSpec);
        switch (specMode) {
            case MeasureSpec.EXACTLY:
                result = specSize;
                break;
            case MeasureSpec.AT_MOST:
            case MeasureSpec.UNSPECIFIED:
            default:
                result = mTextBounds.height() + getPaddingTop() + getPaddingBottom();
                result = Math.min(result, specSize);
                break;
        }
        return result;
    }

    private int measuredHeight(int measureSpec) {
        int result = 0;
        int specMode = MeasureSpec.getMode(measureSpec);
        int specSize = MeasureSpec.getSize(measureSpec);
        switch (specMode) {
            case MeasureSpec.EXACTLY:
                result = specSize;
                break;
            case MeasureSpec.AT_MOST:
            case MeasureSpec.UNSPECIFIED:
            default:
                result = mTextBounds.width() + getPaddingLeft() + getPaddingRight();
                result = Math.min(result, specSize);
                break;
        }
        return result;
    }

    @Override
    protected void onDraw(Canvas canvas) {
        drawText(canvas);
        drawRectLine(canvas);
    }

    private void drawText(Canvas canvas) {
        int startX = (getWidth() - mTextBounds.height() >> 1);
        int startY = (getHeight() - mTextBounds.width() >> 1);
        int stopX = (getWidth() - mTextBounds.height() >> 1);
        int stopY = (getHeight() + mTextBounds.width() >> 1);
        mPath.moveTo(startX, startY);
        mPath.lineTo(stopX, stopY);
        canvas.drawTextOnPath(mTime, mPath, 0, 0, getPaint());
    }

    private void drawRectLine(Canvas canvas) {
        mTextBoundInners.left = PADDING;
        mTextBoundInners.bottom = getHeight() - PADDING;
        mTextBoundInners.top = PADDING;
        mTextBoundInners.right = getWidth() - PADDING;
        getPaint().setColor(getResources().getColor(R.color.white));
        getPaint().setStyle(Paint.Style.STROKE);
        canvas.drawRect(mTextBoundInners, getPaint());
    }
}
