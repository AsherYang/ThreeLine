package com.asher.threeline.ui.view;

import android.content.Context;
import android.content.res.TypedArray;
import android.graphics.Canvas;
import android.graphics.Paint;
import android.graphics.Rect;
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
    private byte[] mBytes;
    private float[] mPoints;
    private Rect mRect = new Rect();
    private int mSpectrumNum = 48;

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
        mBytes = null;
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

    private void updateVisualizer(byte[] fft) {
        byte[] model = new byte[fft.length / 2 + 1];
        model[0] = (byte) Math.abs(fft[0]);

        for (int i = 2, j = 1; j < mSpectrumNum;) {
            model[j] = (byte) Math.hypot(fft[i], fft[i+1]);
            i += 2;
            j++;
        }
        mBytes = model;
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

    // TODO: 17/7/14 need do by Visualizer
    private void drawRect(Canvas canvas, int lineCount) {
        if (mBytes == null) {
            return;
        }
        if (mPoints == null || mPoints.length < mBytes.length * 4) {
            mPoints = new float[mBytes.length * 4];
        }
        mRect.set(0, 0, getWidth(), getHeight());

        // 绘制频谱
        final int basX = mRect.width() / mSpectrumNum;
        final int height = mRect.height();

        for (int i = 0; i < mSpectrumNum; i++) {
            if (mBytes[i] < 0) {
                mBytes[i] = 127;
            }

            final int xi = basX * i + basX / 2;
            mPoints[i * 4] = xi;
            mPoints[i * 4 + 1] = height;

            mPoints[i * 4 + 2] = xi;
            mPoints[i * 4 + 3] = height - mBytes[i];
        }

        canvas.drawLines(mPoints, mPaint);
    }
}
