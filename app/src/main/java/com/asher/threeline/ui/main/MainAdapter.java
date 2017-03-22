package com.asher.threeline.ui.main;

import android.animation.Animator;
import android.animation.AnimatorSet;
import android.animation.ObjectAnimator;
import android.content.Context;
import android.support.v7.widget.RecyclerView;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.view.animation.PathInterpolator;
import android.widget.TextView;

import com.asher.threeline.R;

import java.util.List;

/**
 * Created by ouyangfan on 17/3/22.
 */

public class MainAdapter extends RecyclerView.Adapter<RecyclerView.ViewHolder> {

    private Context mContext;
    private List<String> mData;
    private int mLastPosition = -1;

    public MainAdapter(Context context, List<String> list) {
        this.mContext = context;
        mData = list;
    }

    @Override
    public RecyclerView.ViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(mContext).inflate(R.layout.item_rv_main, parent, false);
        return new MyViewHolder(view);
    }

    @Override
    public void onBindViewHolder(RecyclerView.ViewHolder holder, int position) {
        ((MyViewHolder) holder).name.setText(mData.get(position));

        int adapterPosition = holder.getAdapterPosition();
        int layoutPosition = holder.getLayoutPosition();

        Log.i("TAG", "adapter Pos = " + adapterPosition + " , layout pos = " +
                layoutPosition + " , last pos = " + mLastPosition);

        if (adapterPosition > mLastPosition) {
            startAnimator(holder.itemView, true);
        } else {
            startAnimator(holder.itemView, false);
        }
        mLastPosition = adapterPosition;
    }

    @Override
    public int getItemCount() {
        return mData.size();
    }

    class MyViewHolder extends RecyclerView.ViewHolder {

        private final TextView name;

        public MyViewHolder(View itemView) {
            super(itemView);
            name = (TextView) itemView.findViewById(R.id.tv_item_name);
        }
    }

    private void startAnimator(final View view, boolean isPull) {
        float height = view.getMeasuredHeight() / 3;
        if (!isPull) {
            height = -height;
        }
        if (android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.LOLLIPOP) {
            ObjectAnimator rotationX = ObjectAnimator.ofFloat(view, "translationY", height, 0);
            rotationX.addListener(new Animator.AnimatorListener() {
                @Override
                public void onAnimationStart(Animator animator) {
                    Log.i("TAG", "---- onAnimationStart ----");
                }

                @Override
                public void onAnimationEnd(Animator animator) {
                    Log.i("TAG", "---- onAnimationEnd ----");
                }

                @Override
                public void onAnimationCancel(Animator animator) {

                }

                @Override
                public void onAnimationRepeat(Animator animator) {

                }
            });
            PathInterpolator interpolator = new PathInterpolator(0f, 0f, 0.40f, 1f);
            AnimatorSet animSet = new AnimatorSet();
            animSet.setInterpolator(interpolator);
            animSet.setDuration(400);
            animSet.play(rotationX);
            animSet.start();
        }

    }
}
