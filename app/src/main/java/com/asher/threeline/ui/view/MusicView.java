package com.asher.threeline.ui.view;

import android.content.Context;
import android.content.res.TypedArray;
import android.graphics.Canvas;
import android.graphics.Paint;
import android.util.AttributeSet;
import android.util.Log;
import android.view.View;

import com.asher.threeline.R;

/**
 * Created by ouyangfan on 2017/7/1.
 * <p>
 * 音乐界面 MusicView
 */
public class MusicView extends View {

    private static final String TAG = "MusicView";
    private static final int DEFAULT_WIDTH = 150;
    private static final int DEFAULT_HEIGHT = 70;
    // color
    private int mViewColor;
    // 间隔大小
    private int mInterval;
    // 单条线的宽度
    private int mLineWidth;
    private Paint mPaint = new Paint();

    public MusicView(Context context) {
        this(context, null);
    }

    public MusicView(Context context, AttributeSet attrs) {
        this(context, attrs, 0);
    }

    public MusicView(Context context, AttributeSet attrs, int defStyleAttr) {
        super(context, attrs, defStyleAttr);
        init(context, attrs);
        initPaint();
    }

    private void init(Context context, AttributeSet attrs) {
        TypedArray array = context.obtainStyledAttributes(attrs, R.styleable.MusicView);
        mViewColor = array.getColor(R.styleable.MusicView_android_color,
                getResources().getColor(R.color.color_1d1f3e));
        mInterval = array.getDimensionPixelSize(R.styleable.MusicView_intervalSize,
                getResources().getDimensionPixelSize(R.dimen.dimen_5dp));
        mLineWidth = array.getDimensionPixelSize(R.styleable.MusicView_lineWidth,
                getResources().getDimensionPixelSize(R.dimen.dimen_2dp));
        array.recycle();
        Log.i(TAG, "mInterval = " + mInterval + " , mLineWidth = " + mLineWidth);
    }

    private void initPaint() {
        mPaint.setColor(mViewColor);
        mPaint.setAntiAlias(true);
        mPaint.setStyle(Paint.Style.FILL);
    }

    private void setColor(int color) {
        mPaint.setColor(color);
        invalidate();
    }

    @Override
    protected void onMeasure(int widthMeasureSpec, int heightMeasureSpec) {
        setMeasuredDimension(measureWidth(widthMeasureSpec), measureHeight(heightMeasureSpec));
    }

    private int measureWidth(int widthSpec) {
        int widthMode = MeasureSpec.getMode(widthSpec);
        int widthSize = MeasureSpec.getSize(widthSpec);
        int result = DEFAULT_WIDTH;
        if (widthMode == MeasureSpec.EXACTLY) {
            result = widthSize;
        } else if (widthMode == MeasureSpec.AT_MOST) {
            result = Math.min(result, widthSize);
        }
        return result;
    }

    private int measureHeight(int heightSpec) {
        int heightMode = MeasureSpec.getMode(heightSpec);
        int heightSize = MeasureSpec.getSize(heightSpec);
        int result = DEFAULT_HEIGHT;
        if (heightMode == MeasureSpec.EXACTLY) {
            result = heightSize;
        } else if (heightMode == MeasureSpec.AT_MOST) {
            result = Math.min(result, heightSize);
        }
        return result;
    }

    @Override
    protected void onDraw(Canvas canvas) {
        super.onDraw(canvas);
        Log.i(TAG, "measureWidth = " + getMeasuredWidth() + " , width = " + getWidth()
                + " , measureHeight = " + getMeasuredHeight() + " , height = " + getHeight());
        // 计算线条的个数 mLineWidth * x + mInterval * (x-1) = getWidth()
        int lineCount = (getWidth() + mInterval) / (mLineWidth + mInterval);

        Log.i(TAG, "lineCount = " + lineCount);
        drawRect(canvas, lineCount);
    }

    private void drawRect(Canvas canvas, int lineCount) {
        for (int i = 0; i < lineCount; i++) {
            canvas.drawRect(i * mLineWidth + i * mInterval, 0,
                    (i + 1) * mLineWidth + i * mInterval, getHeight(), mPaint);
        }
    }
}
